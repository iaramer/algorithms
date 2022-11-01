import sys
import pickle
from typing import Any, Dict, List
import pandas as pd
import numpy as np
from collections import defaultdict as ddict
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
import json
import warnings

warnings.filterwarnings("ignore")


ARTIFACTS_FILE = "artifacts.pkl"
RESULTS_FILE_NAME = "results.csv"


def gen_date(df: pd.DataFrame, date_feature_name='date') -> pd.DataFrame:
    """
    This function generates a set of date related features.
    
    :param df: The initial dataset with the "date" feature. 
    :param date_feature_name: The name of the "date" feature. 
    :return: The dataframe with the generated features.
    """
    
    df = df[[date_feature_name]].copy()
    df[date_feature_name] = pd.to_datetime(df[date_feature_name], format='%Y-%m-%d')
        
    df['sin_minute'] = np.sin(2*np.pi*df[date_feature_name].dt.minute/60)
    df['cos_minute'] = np.cos(2*np.pi*df[date_feature_name].dt.minute/60)
    df['sin_hour'] = np.sin(2*np.pi*df[date_feature_name].dt.hour/24)
    df['cos_hour'] = np.cos(2*np.pi*df[date_feature_name].dt.hour/24)

    dw_mapping={
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', \
        5: 'Saturday', 6: 'Sunday'
    }
    df['day_of_week'] = df[date_feature_name].dt.weekday.map(dw_mapping)
    for v in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', \
              'Saturday', 'Sunday']:
        df[v] = df['day_of_week'] == v
        df[v] = df[v].astype(int)
    df.drop('day_of_week', axis=1, inplace=True) 

    df.drop(date_feature_name, axis=1, inplace=True)
    return df


def to_dict(x):
    """
    A mapping function from list to dict.
    """
    res = ddict(int)
    for xx in x:
        res[xx['site']] += xx['length']
    return res


def load_data() -> pd.DataFrame:
    """
    This function reads the CLI argument with the dataset path and loads the dataset.
    
    :return: The dataset for prediction.
    """
    args = sys.argv
    if len(args) != 2:
        raise Exception(f"The number of the arguments doesn't match!")
    data_path = args[1]
    d = None
    with open(data_path) as f:
        d = json.load(f)
    if not d:
        raise Exception(f"The dataset not found in the path: \"{data_path}\"!")
    return pd.DataFrame(d)


def load_artifacts() -> Dict[str, Any]:
    """
    This function loads the artifacts.
    
    :return: The dict with the artifacts.
    """
    file = ARTIFACTS_FILE
    artifacts = None
    with open(file, 'rb') as f:
        artifacts = pickle.load(f)
    if not artifacts:
        raise Exception(f"The file with artifacts \"{file}\" not found!")
    return artifacts


def session_total_time(x):
    """
    Dummy function.
    """
    return sum([site['length'] for site in x])


def session_avg_time(x):
    """
    Dummy function.
    """
    return sum([site['length'] for site in x]) / len(x)


def preprocess(df: pd.DataFrame, scaler: StandardScaler, columns: List[str],
               topn_sites_features: List[str]) -> pd.DataFrame:
    """
    This function preprocesses the dataset for prediction.
    
    :return: The preprocessed dataset.
    """
    df = df.copy()

    if 'user_id' in df.columns:
    	df.drop('user_id', axis=1, inplace=True)

    df['datetime'] = pd.to_datetime(df['date'] + ':' + df['time'], format = '%Y-%m-%d:%H:%M:%S')
    df_dt = gen_date(df, date_feature_name='datetime')
    df = pd.concat([df, df_dt], axis=1)
    df = df.drop(['date', 'time', 'datetime'], axis=1)

    df['locale_ru'] = df['locale'] == "ru-RU"
    df_dum = pd.get_dummies(df[['browser', 'os', 'gender', 'locale_ru', 'location']], drop_first=True)
    df = pd.concat([df, df_dum], axis=1)
    df = df.drop(['browser', 'os', 'gender', 'locale_ru', 'locale', 'location'], axis=1)

    df['session_total_time'] = df['sites'].apply(session_total_time)
    df['session_avg_time'] = df['sites'].apply(session_avg_time)
    df['session_n_sites'] = df['sites'].apply(lambda x: len(x))

    df['sites'] = df['sites'].apply(to_dict)
    for col in topn_sites_features:
        df[col] = df['sites'].apply(lambda x: x[col] if col in x else 0.0)
    df = df.drop(['sites'], axis=1)

    top_n = len(topn_sites_features)
    cols_to_scale = df.columns[-top_n-3:]
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])
    return df[columns]


def save_pred(arr: np.array) -> None:
    """
    This function saves the predictions to a file.
    """
    with open(RESULTS_FILE_NAME, 'w') as f:
        res = '\n'.join(str(x) for x in arr ^ 1)
        f.write(res)


if __name__ == "__main__":
    print("(1/4) Loading the data and the artifacts...")
    df = load_data()
    artifacts = load_artifacts()

    print("(2/4) Preprocessing...")
    scaler = artifacts['scaler']
    topn_sites_features = artifacts['topn_sites_features']
    cols = artifacts['columns']
    X = preprocess(df, scaler, cols, topn_sites_features)

    print("(3/4) Predicting...")
    xgb = artifacts['xgb']
    y_pred = xgb.predict(X)

    print("(4/4) Saving the results...")
    save_pred(y_pred)
    print("Finished successfully.")

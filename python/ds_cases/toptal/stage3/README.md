# Task details

## Dataset

Download the dataset here:
https://drive.google.com/file/d/1yXPQF3ED6pFLBiKsr-BL3fu-t0yY7KAY/view?usp=sharing

The dataset contains data about user sessions that have been recorded over a period of
time. The dataset consists of two parts: the training dataset where user ID's are labeled, and
the verification set without labels.

Each session is represented by a JSON object with the following fields:
* "user_id" is the unique identifier of the user.
* "browser", "os", "locale" contain info about the software on the user's machine.
* "gender", "location" give analytics data about the user.
* "date" and "time" is the moment when the session started (in GMT).
* "sites" is a list of up to 15 sites visited during the session. For each site, the URL and
the length of visit in seconds are given.

## Requirements

The goal is to create a method to identify the user with id=0 (codename Joe) specifically.

Your solution should contain:
* Exploratory data analysis, either as a standalone report/presentation or in the form of
a Jupyter notebook
* A standalone script that runs the whole pipeline on the verification set and creates a
file where each line is the predicted label (0 = Joe, 1 = not Joe)
* File result.csv containing the predictions for the test set.

## Additional

Milestones and task delivery:
* The deadline to submit your completed project is 1 week from the moment you
received the project requirements.
* It means the project code must be submitted within 1 week from the moment that was
delivered to you by email.
* If you schedule your final interview after the 1-week deadline, make sure to submit
your completed project and all code to the private repository before the deadline
* Everything that is submitted after the deadline will not be taken into consideration.
* Please do not commit any code at least 6 hours before the meeting time so that it can
be reviewed. Anything that is submitted after this time will not be taken into
consideration.
* Please join the meeting room for this final interview on time. If you miss your interview
without providing any prior notice, your application may be paused for six months.

# Summary

The notebook contains the following sections:

1. Setup
    * imports
    * constants
    * functions
2. Data
    * EDA
    * Presprocessing
3. Model
    * Baseline
    * Advanced algorithm
4. Final algorithm

# The script

#### Installation

Make sure you set up the environment from the `requrements.txt`.

#### Usage

Simply run the `script.py` in the CLI:
```python
python -m script "file_name.json"
```
from collections import OrderedDict
from sklearn.base import TransformerMixin
from typing import List, Union
import numpy as np
from collections import Counter
from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer()


class BoW(TransformerMixin):
    """
    Bag of words tranformer class
    
    check out:
    https://scikit-learn.org/stable/modules/generated/sklearn.base.TransformerMixin.html
    to know about TransformerMixin class
    """

    def __init__(self, k: int):
        """
        :param k: number of most frequent tokens to use
        """
        self.k = k
        # list of k most frequent tokens
        self.bow = None

    def fit(self, X: np.ndarray, y=None):
        """
        :param X: array of texts to be trained on
        """
        # task: find up to self.k most frequent tokens in texts_train,
        # sort them by number of occurences (highest first)
        # store most frequent tokens in self.bow
        # raise NotImplementedError
        text = [tokenizer.tokenize(x) for x in X]
        c = Counter([x for y in text for x in y])
        self.bow = [x[0] for x in c.most_common(self.k)]
        # fit method must always return self
        return self

    def _text_to_bow(self, text: str) -> np.ndarray:
        """
        convert text string to an array of token counts. Use self.bow.
        :param text: text to be transformed
        :return bow_feature: feature vector, made by bag of words
        """

        # result = None
        # raise NotImplementedError
        result = [0] * len(self.bow)
        for token in tokenizer.tokenize(text):
            if token in self.bow:
                result[self.bow.index(token)] += 1
        return np.array(result, "float32")

    def transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        :param X: array of texts to transform
        :return: array of transformed texts
        """
        assert self.bow is not None
        return np.stack([self._text_to_bow(text) for text in X])

    def get_vocabulary(self) -> Union[List[str], None]:
        return self.bow


class TfIdf(TransformerMixin):
    """
    Tf-Idf tranformer class
    if you have troubles implementing Tf-Idf, check out:
    https://streamsql.io/blog/tf-idf-from-scratch
    """

    def __init__(self, k: int = None, normalize: bool = False):
        """
        :param k: number of most frequent tokens to use
        if set k equals None, than all words in train must be considered
        :param normalize: if True, you must normalize each data sample
        after computing tf-idf features
        """
        self.k = k
        self.normalize = normalize
        self.word_set = set()
        self.total_docs = 0
        self.word_count = None
        self.word_index = {}

        # self.idf[term] = log(total # of documents / # of documents with term in it)
        self.idf = OrderedDict()

    def count_dict(self, sentences):
        count_dict = {}
        for word in self.word_set:
            count_dict[word] = 0
        for sent in sentences:
            for word in sent:
                count_dict[word] += 1
        return count_dict

    def term_frequency(self, document, word):
        N = len(document)
        occurance = len([token for token in document if token == word])
        return occurance / N      

    def inverse_document_frequency(self, word):
        word_occurance = self.word_count[word] + 1 if word in self.word_count else 1
        return np.log(self.total_docs / word_occurance)

    def fit(self, X: np.ndarray, y=None):
        """
        :param X: array of texts to be trained on
        """
        # raise NotImplementedError
        sentences = []
        self.total_docs = len(X)
        for sent in X:
            sentences.append(tokenizer.tokenize(sent))
        all_words = []
        for sentence in sentences:
            for word in sentence:
                all_words.append(word)
        self.word_count = dict(Counter(all_words).most_common(self.k))
        for sent in sentences:
            for word in sent:
                if word in self.word_count:
                    self.word_set.add(word)
        for i, word in enumerate(self.word_set):
            self.word_index[word] = i
        # fit method must always return self
        return self

    def _text_to_tf_idf(self, text: str) -> np.ndarray:
        """
        convert text string to an array tf-idfs.
        *Note* don't forget to normalize, when self.normalize == True
        :param text: text to be transformed
        :return tf_idf: tf-idf features
        """
        vec = np.zeros((self.k,))
        sentence = tokenizer.tokenize(text)
        for word in sentence:
            tf = self.term_frequency(sentence, word)
            idf = self.inverse_document_frequency(word)
            if word in self.word_index:
                vec[self.word_index[word]] = tf * idf + 1
            # I omit OOV because there are only 30 mins left until the submission deadline
        # result = None
        # raise NotImplementedError
        return np.array(vec, "float32")

    def transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        :param X: array of texts to transform
        :return: array of transformed texts
        """
        assert self.idf is not None
        return np.stack([self._text_to_tf_idf(text) for text in X])

__author__ = 'Alex'

from sklearn import svm
import numpy as np
from sklearn import cross_validation
from sklearn import datasets

def train(data, k):
    """
    Perform k-fold cross validation of SVM
    :param data:
    Data for validation
    :param k:
    # of folds
    :return:
    """
    clf = svm.SVC()

    scores = cross_validation.cross_val_score(clf, data.data, data.target, cv=k)

    return clf, scores.mean(), scores.std() * 2


if __name__=='__main__':

    iris = datasets.load_iris()

    tr = train(iris, 10)

    print "Accuracy: %0.2f (+/- %0.2f)" % (tr[1], tr[2])
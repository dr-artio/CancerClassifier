__author__ = 'Alex'

from sklearn import svm, grid_search
import numpy as np
from sklearn import cross_validation
import json

def grid_search_cv(samples, targets, data, k, tuned_params):
    mycv = cross_validation.StratifiedKFold(targets, n_folds = k)
    svr = svm.LinearSVC()

    print mycv

    clf = grid_search.GridSearchCV(svr, tuned_params, cv=mycv)
    clf.fit(data, targets)
    print clf.best_params_
    return clf.best_estimator_


def parse_json(target_names):
    samples = []
    data = []
    targets = []

    for k in target_names:
        with open(target_names[k]) as fp:
            d = json.load(fp)
            for patient, expressions in d.items()[:10]:
                samples.append(patient)
                s_expressions = sorted(expressions)
                def check(x):
                    if x in expressions:
                        return expressions[x]
                    else:
                        return 0.0
                data.append(map(check, s_expressions))
                targets.append(k)
    return samples, targets, data


def train(clf, samples, targets, data, k):
    """
    Perform k-fold cross validation of SVM
    :param data:
    Data for validation
    :param k:
    # of folds
    :return:
    """

    scores = cross_validation.cross_val_score(clf, data, targets, cv=k)
    print scores
    return clf, scores.mean(), scores.std() * 2


if __name__=='__main__':

    #iris = datasets.load_iris()
    #
    # tr = train(iris, 10)
    #
    # print "Accuracy: %0.2f (+/- %0.2f)" % (tr[1], tr[2])
    target_names = {0: 'bladder.json', 1:'blood.json', 2: 'brain.json',
                    3: 'breast.json', 4:'cervix.json', 5: 'colorectal.json',
                    6: 'headneck.json', 7: 'kidney.json', 8: 'liver.json',
                    9: 'lung.json', 10: 'ovary.json', 11: 'pancreas.json',
                    12: 'prostate.json', 13: 'skin.json', 14: 'uterus.json'
                }
    samples, targets, data = parse_json(target_names)
    print 'Loading finished!'

    target_indices = np.array(targets)

    parameters = {'C':[0.5] }
    print "Grid search..."
    clf = svm.LinearSVC() #grid_search_cv(samples, target_indices, data, 3, parameters)
    print "Validation..."
    tr = train(clf, samples, target_indices, data, 10)
    print "Accuracy: %0.2f (+/- %0.2f)" % (tr[1], tr[2])
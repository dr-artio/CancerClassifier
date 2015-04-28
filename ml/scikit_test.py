__author__ = 'Alex'

from sklearn import svm, grid_search, ensemble
import numpy as np
from sklearn import cross_validation
from collections import Counter
import pickle
import json

def grid_search_cv(samples, targets, data, k, tuned_params):
    mycv = cross_validation.StratifiedKFold(targets, n_folds = k)
    svr = svm.LinearSVC()
    #svr = svm.SVC()
    #svr = ensemble.RandomForestClassifier()

    print mycv

    clf = grid_search.GridSearchCV(svr, tuned_params, cv=mycv)
    clf.fit(data, targets)
    print clf.best_params_
    print clf.best_estimator_.predict(data[0])
    print len(data[0])
    pickle.dump(clf.best_estimator_, open('SVMlin.pkl', 'w+'))
    return clf.best_estimator_

def get_common_ids(target_names):
    c = Counter()
    for k in target_names:
        with open(target_names[k]) as fp:
            d = json.load(fp)
            for x in d:
                for y in d[x]:
                    c[y] += 1
    mv = c.most_common(1)[0][1]

    fc = filter(lambda x: c[x] == mv, c)
    return sorted(fc)

def parse_json(target_names):
    samples = []
    data = []
    targets = []
    s_expressions = get_common_ids(target_names)
    # print len(s_expressions)
    # print s_expressions
    for k in target_names:
        with open(target_names[k]) as fp:
            d = json.load(fp)
            for patient, expressions in d.items():
                samples.append(patient)
                data.append(map(lambda x: expressions[x], s_expressions))
                targets.append(k)
    # data = preprocessing.scale(data)

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

    scores = cross_validation.cross_val_score(clf, data, targets, cv=k, n_jobs=-1, scoring='accuracy')
    print scores
    return clf, scores.mean(), scores.std() * 2


if __name__=='__main__':

    #iris = datasets.load_iris()
    #
    # tr = train(iris, 10)
    #
    # print "Accuracy: %0.2f (+/- %0.2f)" % (tr[1], tr[2])
    target_names = {0: 'bladder.json', 1:'blood.json', 2: 'brain.json',
                    3: 'breast.json', 4:'cervix.json'#, 5: 'colorectal.json',
                    # 6: 'headneck.json', 7: 'kidney.json', 8: 'liver.json',
                    #9: 'lung.json', 10: 'ovary.json', 11: 'pancreas.json',
                    # 12: 'prostate.json', 13: 'skin.json', 14: 'uterus.json'
                }
    samples, targets, data = parse_json(target_names)
    print 'Loading finished!'

    target_indices = np.array(targets)

    parameters = {'C':[10], 'class_weight':['auto'],
                  'multi_class':['ovr'], 'penalty':['l2'] }
   # parameters =  {'C': [1, 10, 100], 'gamma': [0.001, 0.0001], 'kernel': ['rbf', 'poly']}
    #parameters = {"n_estimators": [10, 20, 50], "n_jobs": [-1],"class_weight":['auto','subsample', None] }
    print "Grid search..."
    clf = grid_search_cv(samples, target_indices, data, 5, parameters)
    print "Validation..."
    tr = train(clf, samples, target_indices, data, 5)
    print "Accuracy: %0.2f (+/- %0.2f)" % (tr[1], tr[2])
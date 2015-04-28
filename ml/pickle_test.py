__author__ = 'Alex'

import pickle
import numpy as np


if __name__=='__main__':

    svr = pickle.load(open('SVMlin2.pkl'))
    print svr.predict(np.random.rand(18163))
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:26:24 2021

@author: thiago
"""


import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import copy

X = np.array([0.5, 1.2, 2.1, 3.5, 5.4])
y = np.array([5.1, 3.2, 2.8, 1, 0.4])

X = np.c_[np.ones((5, 1)), X]

theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

xNovo = np.array([0.5, 1.2, 2.1, 3.5, 5.4])

xNovo = np.c_[np.ones((5, 1)), xNovo]
yNovo = xNovo.dot(theta)

plt.plot(xNovo[:,1], yNovo, "red")
plt.plot( X[:,1], y, "b.")
#plt.axis([0,2,0,3])
plt.show()

r2 = r2_score(y, yNovo)
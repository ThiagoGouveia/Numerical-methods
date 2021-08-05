# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:26:24 2021

@author: thiago
"""


import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


X = 2 * np.random.rand(50,1)
y = X + np.random.rand(50,1)

X = np.c_[np.ones((50, 1)), X]

theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

xNovo = 2 * np.random.rand(50,1)

xNovo = np.c_[np.ones((50, 1)), xNovo]
yNovo = xNovo.dot(theta)

plt.plot(xNovo[:,1], yNovo, "red")
plt.plot( X[:,1], y, "b.")
plt.axis([0,2,0,3])
plt.show()

r2 = r2_score(y, yNovo)
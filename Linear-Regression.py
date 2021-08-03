# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:26:24 2021

@author: thiago
"""


import numpy as np
import matplotlib.pyplot as plt

x = 2 * np.random.rand(50,1)
y = x + np.random.rand(50,1)

x_b = np.c_[np.ones((50, 1)), x]
theta_best = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)

x_new = np.array([[0],[2],[4],[6]])

x_new_b = np.c_[np.ones((4, 1)), x_new]
y_predict = x_new_b.dot(theta_best)

plt.plot(x_new, y_predict, "r-")
plt.plot(x, y, "b.")
plt.axis([0,2,0,3])
plt.show()


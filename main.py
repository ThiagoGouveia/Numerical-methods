import Gaussian_Elimination as g
import numpy as np

n = 3  
A = np.array([[1, -3, 2], [-2, 8, -1], [4, -6, 5]])
b = np.array([11, -15, 29])


resultado = g.gaussElimination(A,b,n)

print(resultado)
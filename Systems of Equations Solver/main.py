import Gaussian_Elimination as g
import Gaussian_Pivot as gp
import Gaussian_LU as LU
import numpy as np

n = 3  
A = np.array([[1, -3, 2], [-2, 8, -1], [4, -6, 5]], dtype='f')
b = np.array([11, -15, 29], dtype='f')

#res = g.gaussElimination(A,b,n)
#print(res)

#res = gp.gaussPivot(A,b,n)
#print(res)


res = LU.gaussLU(A,b,n)
print(res)


import Forward_Substitution as f
import numpy as np
import copy

def gaussLU(A,b,n):
    P = np.identity(n) # identity array
    
    for j in range(0, n-1, 1):
        p = j
        max = A[j][j]
        for k in range(j+1, n, 1):
            if abs(A[k][j]) > max:
                max = abs(A[k][j])
                p = k
        if(j != p):
            for k in range(0, n, 1):
                t = A[j][k]
                A[j][k] = A[p][k]
                A[p][k] = t
            
            t = copy.deepcopy(P[j])
            P[j] = copy.deepcopy(P[p])
            P[p] = copy.deepcopy(t)
        
        
        if abs(A[j][j]) != 0:
            for i in range(j+1, n, 1):
                m = A[i][j] / A[j][j]
                A[i][j] = m
                for k in range(j+1, n, 1):
                    A[i][k] = A[i][k] - m * A[j][k]

    L = np.tril(A)
    np.fill_diagonal(L, 1)  
    U = np.triu(A)
    
    Pb = np.matmul(P, b)
    
    y = np.matmul(np.linalg.inv(L), Pb)

    x = np.matmul(np.linalg.inv(U), y)

    return x       
            
            
                
        




import numpy as np
def forwardSubstitution(n,L,c):
    x = np.zeros((3,), dtype='f') #creat output array
    x[0] = c[0]/L[0][0] #initialize array 

    j = 0
    for i in range(1, n, 1):
        soma = 0
        for j in range(0, i-1, 1):
            soma = soma + L[i][j] * x[j]
        
        x[i] = (c[i] - soma) / L[i][j]
    
    
    
    
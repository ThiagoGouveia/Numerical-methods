import numpy as np

def gaussSeidel(n, A, b, Toler, iterMax):
    #creat output array
    x = np.zeros((n,), dtype='f')
    v = np.zeros((n,), dtype='f') 
    
    for i in range(n):
        x[i] = b[i] / A[i][i]
    
    Iter = 0
    
    while True:
        Iter = Iter + 1
        normaNum = 0
        normaDen = 0
        for i in range(n):
            Sum = 0
            for j in range(n):
                if i != j:
                    Sum = Sum + A[i][j] * x[j]
            
            v[i] = x[i]
            x[i] = (b[i] - Sum) / A[i][i]
            t = abs(v[i] - x[i])
            
            if t > normaNum:
                normaNum = t
            if abs(x[i]) > normaDen:
                normaDen = abs(x[i])

    
        normaRel = normaNum / normaDen
        
        print("Numero de iterações: ", Iter)
        print("Convergência: ", normaRel)
        print("Vet: ", x)
        
        if normaRel <= Toler or Iter >= iterMax:
            break
    
    if normaRel <= Toler:
        Info = 0
    else:
        Info = 1
        
    return x  
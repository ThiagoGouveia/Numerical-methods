import Backward_Substitution as back

def gaussPivot(A,b,n):
    
    for k in range(0,n-1,1):
        
        maior = abs(A[k][k])
        for i in range(k+1, n, 1):
            if abs(A[i][k]) > maior:
                maior = abs(A[i][k])
                r = i
            else: 
                r = k
        
        for i in range(0, n, 1):
            v = A[k][i]
            A[k][i] = A[r][i]
            A[r][i] = v 
        
        v = b[k]
        b[k] = b[r]
        b[r] = v
        
        
        for i in range(k+1, n, 1):
            
            m = (-1) * A[i][k] / A[k][k]
            for j in range (k, n, 1):
                A[i][j] = A[i][j] + m * A[k][j] 
                
                
            b[i] = b[i] + m * b[k]
                  
    return back.backSubstitution(n, A, b)


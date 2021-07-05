import Backward_Substitution as back

def gaussElimination(A,b,n):
    
    for k in range(0,n-1,1):
        for i in range(k+1, n,1):
            m = (-1) * A[i][k] / A[k][k]
            for j in range (k, n, 1):
                A[i][j] = A[i][j] + m * A[k][j]
            b[i] = b[i] + m * b[k] 
    
    return back.backSubstitution(n, A, b)

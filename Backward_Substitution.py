def backSubstitution(n,U,d):
    
    x = d/U.diagonal()
    
    for i in range(n-1, 0,-1):
        
        Soma = 0
        
        for j in range(i+1,n,1):
            Soma = Soma +U[i][j] * x[j]
        x[i] = (d[i]-Soma)/U[i][i]
    
    return x
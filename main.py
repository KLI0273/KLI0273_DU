import scipy.sparse as sparse
import numpy as np

def pocet_sousedu(i,j,n):
    if((i != 0 and i != n-1) and (j != 0 and j != n-1)): return 4
    elif(i,j == 0,0 or n-1,n-1 or n-1,n or n,n-1): return 2
    else: return 3

def create_vertex(n, diag_coeficient):
    matrix = np.ones((n,n))*0
    first = 1
    for m in range(n):
        for s in range(n):
            if(m == s):
                k = pocet_sousedu(m,s,n)
                if(k == 2 and first == 0):
                    matrix[m-1,s] = -epsilon
                    matrix[m,s-1] = -epsilon
                    matrix[m,s] = 1+(k*epsilon)
                if(k == 2 and first == 1):
                    matrix[m+1,s] = -epsilon
                    matrix[m,s+1] = -epsilon
                    first = 0
                    matrix[m,s] = 1+(k*epsilon)
                if(k == 4):
                    matrix[m,s-1:s+2] = -epsilon
                    matrix[m-1:m+2,s] = -epsilon
                    matrix[m,s] = 1+(k*epsilon)-diag_coeficient
    return matrix

def diag(n):
    matrix = np.ones((n,n))*0
    for m in range(n):
        for s in range(n):
            if(m==s):matrix[m,s] = -epsilon
    return matrix

n = 6
epsilon = 1e-1
A = sparse.lil_matrix((n*n, n*n))
diag_coeficient = epsilon
pocet_iteraci = 1

for i in range(n):
    for j in range(n):
        if(i==j):
            vertex = create_vertex(n, diag_coeficient)
            A[i*n:n*(i+1), j*n:n*(j+1)] = vertex
            
            if(n/pocet_iteraci > n/(n/2) and n%2 == 1):
                diag_coeficient -= epsilon
                pocet_iteraci += 1
            elif(n/pocet_iteraci >= n/(n/2) and n%2 == 0):
                if(n/pocet_iteraci != n/(n/2)):
                    diag_coeficient -= epsilon
                pocet_iteraci += 1
            else:
                diag_coeficient += epsilon
                pocet_iteraci += 1


            

        if(i+1 == j or j+1 ==i):
            matri = diag(n)
            A[i*n:n*(i+1), j*n:n*(j+1)] = matri

print(A.todense())
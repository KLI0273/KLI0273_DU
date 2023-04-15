import scipy.sparse as sparse
import numpy as np



def pocet_sousedu(i,j,n):
    if((i != 0 and i != n-1) and (j != 0 and j != n-1)): return 4
    elif(i,j == 0,0 or n-1,n-1 or n-1,n or n,n-1): return 2
    else: return 3

def create_vertex(n):
    matrix = np.ones((n,n))*0
    for m in range(n):
        for s in range(n):
            if(m == s):
                k = pocet_sousedu(m,s,n)
                matrix[m,s] = 1+(k*epsilon)
                if(k == 4):
                    matrix[m,s-1] = -epsilon
                    matrix[m,s+1] = -epsilon
                    matrix[m-1,s] = -epsilon
                    matrix[m+1,s] = -epsilon
    return matrix

n = 3
epsilon = 1e-1
A = sparse.lil_matrix((n*n, n*n))
# TODO fill matrix A - diagonal and non-diagonal elements
for i in range(n):
    for j in range(n):
        if(i==j):
            vertex = create_vertex(n)
            print(np.shape(vertex))
            A[i*n:n*(i+1), j*n:n*(j+1)] = vertex


print(A.todense())
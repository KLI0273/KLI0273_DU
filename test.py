import scipy.sparse as sparse
import numpy as np
import matplotlib.pyplot as plt

def vyp_eps(i,j):
    odecti = 0
    if(i==0 or j==0 or i==n-1 or j==n-1): odecti += epsilon
    if((i==0 and j==0) or (i==0 and j==n-1) or (i==n-1 and j==0) and (i==n-1 and j==n-1)): odecti += epsilon
    return odecti

n = 3
epsilon = 1e-1
A = sparse.lil_matrix((n*n, n*n))
for i in range(n):
    for j in range(n):
        if(j+n+(n*i)<n*n): A[j+(n*i),j+n+(n*i)] = -epsilon
        if(j+n+(n*i)<n*n): A[j+n+(n*i), j+(n*i)] = -epsilon
        if(i != n-1): A[n*j+i,n*j+1+i] = -epsilon
        if(i != n-1): A[n*j+1+i,n*j+i] = -epsilon
        A[i*n+j,i*n+j] = ((1+epsilon*4) - vyp_eps(i,j) )

print(A.todense())
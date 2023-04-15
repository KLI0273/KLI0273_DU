import numpy as np

A = np.array(([1,2,3],[4,5,6],[7,8,9]))*0
n, s = 1,1
A[n-1:n+2,s] = 1
print(A)
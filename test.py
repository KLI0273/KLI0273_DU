import numpy as np
import scipy.sparse as sparse

n = 3
epsilon = 0.1

col1 = np.arange(1, n*n-n+1) + n-1
row1 = np.arange(0, n*n-n)
col2 = np.arange(1, n*n-n+1)-1
row2 = np.arange(0, n*n-n) +n

data = -epsilon * np.ones((n * n - n)*2)
row = np.vstack((row1, row2)).reshape((-1,), order='F')
col = np.vstack((col1, col2)).reshape((-1,), order='F')

csr = sparse.csr_matrix((data, (row, col)))
print(csr.todense())


"""
col1 = np.arange(1, n*n-n+1) + n-1
row1 = np.arange(0, n*n-n)
col2 = np.arange(1, n*n-n+1)-1
row2 = np.arange(0, n*n-n) +n

data = -epsilon * np.ones((n * n - n)*2)
row = np.vstack((row1, row2)).reshape((-1,), order='F')
col = np.vstack((col1, col2)).reshape((-1,), order='F')

csr = sparse.csr_matrix((data, (row, col)))
print(csr.todense())

print(row_indices)
print(col_indices)
print(data)
"""
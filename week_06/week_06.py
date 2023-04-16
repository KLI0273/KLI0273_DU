import scipy.sparse as sparse
import numpy as np

def A_efficiently(n, epsilon):
    #Diagonaly -+n
    col1 = np.arange(1, n*n-n+1) + n-1
    row1 = np.arange(0, n*n-n)
    col2 = np.arange(1, n*n-n+1)-1
    row2 = np.arange(0, n*n-n) +n
    data1 = -epsilon * np.ones((n * n - n)*2)

    #Diag02 up
    col3 = np.arange(1, n*n)
    row3 = np.arange(0, n*n-1)
    data3 = -epsilon * np.ones((n * n)-1)
    data3[n-1::n] = 0

    #diag02 down
    row4 = np.arange(1, n*n)
    col4 = np.arange(0, n*n-1)
    data4 = -epsilon * np.ones((n * n)-1)
    data4[n-1::n] = 0

    #diagonala...


    data = np.hstack((data1,data3,data4))
    row = np.hstack((row1,row2,row3,row4))
    col = np.hstack((col1,col2,col3,col4))

    csr = sparse.csr_matrix((data, (row, col)))
    return csr

n = 3
epsilon = 0.1
csr = A_efficiently(n, epsilon)
print(csr.todense())

#print(A_efficiently(n, epsilon).todense())

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


csr = sparse.csr_matrix((data, (row_indices, col_indices)))
print(csr.todense())

print(row_indices)
print(col_indices)
print(data)
"""

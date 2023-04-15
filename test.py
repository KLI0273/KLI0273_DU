
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix, coo_matrix, lil_matrix

data = np.array([1, 2, 4, 5, 6])
row_indices = np.array([0, 0, 2, 2, 2])
col_indices = np.array([0, 2, 0, 1, 2])

# což odpovídá plné matici
full_matrix = np.array([[1, 0, 2],
                        [0, 0, 0],
                        [4, 5, 6]])
# LIL matrix
lil = lil_matrix((3, 3))
lil[0, 0] = 1
lil[0, 2] = 2
lil[2, 0] = 4
lil[2, 1] = 5
lil[2, 2] = 6
print("LIL format:")
print("data:", lil.data)
print("rows:", lil.rows)
print(lil)
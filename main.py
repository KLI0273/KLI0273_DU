import numpy as np
C = np.zeros((8,8))
for i in range(len(C)):
    if(i%2 == 0):C[i][0:8:2]= 1
    if(i%2 == 1):C[i][1:7:2]= 1
print(C)
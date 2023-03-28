import numpy as np
import matplotlib as plt

def integer_spiral(n):
    A = np.zeros([n+2,n+2])
    pos_rows = n//2 +1
    pos_cols = n//2 +1
    i = 1

    A[pos_rows, pos_cols] = i
    i += 1
    pos_rows -= 1

    while(i <= n**2):
        A[pos_rows, pos_cols] = i
        i+=1
        if(A[pos_rows - 1, pos_cols] != 0 and A[pos_rows, pos_cols + 1] == 0):
            pos_cols += 1
        elif(A[pos_rows, pos_cols - 1] != 0):
            pos_rows -= 1
        elif(A[pos_rows + 1, pos_cols] != 0):
            pos_cols -= 1
        else:
            pos_rows += 1

    return A[1:-1, 1:-1]

def integer_spiral_numpy(n):

    B = np.zeros([n+2,n+2], dtype = int)
    b = np.arange(1,n*n+1)
    i,j = n//2 +1, n//2 +1
    current = 1

    for k in range(1): #int((n+1)/2)

        hrana_Up = slice(current, current+2*k+1)
        B[i+k:i-k-1:-1, j+k] = b[hrana_Up]
        current += 2*k+1

        hrana_Left = slice(current, current+2*k+2)
        B[i-k, j+k:j-k-1:-1] = b[hrana_Left]
        current += 2*k+2

        hrana_Down = slice(current, current+2*k+1)
        B[i-k:i+k+1, j-k] = b[hrana_Down]
        current += 2*k+1

        hrana_Right = slice(current, current+2*k+2)
        B[i+k, j-k:j+k+1 ] = b[hrana_Right]
        current += 2*k+2

    return B[1:-1, 1:-1]

B = integer_spiral_numpy(7)
print(B)
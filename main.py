import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(x_min = -2, x_max = 1, y_min = -1.5, y_max = 1.5, n = 1000, k= 100):
    
    y, x = np.mgrid[x_min:x_max:complex(0, n), y_min:y_max:complex(0, n)]#.astype(np.float128)
    c = (x-0.5)+(y+0.5)* 1j
    divergence_matrix = np.zeros((np.shape(c)))+k
    zn = 0
    for i in range(k):
        zn = (zn**2) + c
        for m in range(n):
            for l in range(n):
                if(np.abs(zn[m,l] > 2)):

                    divergence_matrix[m,l] -= 1
                    zn[m,l] = 2
         
    return divergence_matrix

n = 100
k = 100

divergence_matrix = mandelbrot_set(n=n, k=k)
plt.imshow(divergence_matrix) #, cmap='terrain'
plt.show()
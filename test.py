import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(x_min=-2, x_max=1, y_min=-1.5, y_max=1.5, n=1000, k=100):
    x, y = np.mgrid[x_min:x_max:complex(0, n), y_min:y_max:complex(0, n)]
    c = x + y * 1j
    zn = 0
    divergence_matrix = np.zeros((np.shape(c)))

    for i in range(k):
        zn = zn**2 + c
        divergent = np.abs(zn) > 2
        divergent_now = divergent & (divergence_matrix == 0)
        divergence_matrix[divergent_now] = n+1
        zn[divergent] = 2

    return divergence_matrix / np.max(divergence_matrix)

n = 1000
k = 100

divergence_matrix = mandelbrot_set(n=n, k=k)
plt.imshow(divergence_matrix)
plt.show()
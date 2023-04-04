import matplotlib.pyplot as plt
import numpy as np

def r(ot):
    return 2 * np.sin(3*ot)
ot = np.linspace(0,1,100)

plt.polar(ot, r(ot))
plt.title ("PP - Polar Plot", fontsize = 12)
plt.show()
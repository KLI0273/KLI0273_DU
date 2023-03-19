import numpy as np
import math as ma

def odmocnina(a, n): #a = cislo #* n = pocet opakovani cyklu
    if(a == 0):
        return 0
    x=((a/a)+a)/2  
    for i in range(n):
        x = ((a/x)+x)/2 
    return x      

def aproximace_pi(N):
    b = 1
    for i in range(N):
        v = odmocnina(1**2 - (b/2)**2, 100)
        S = 6*b*(v/2)
        if(i>0): S = S*(2**i)
        b = odmocnina((b/2)**2 + (1-v)**2,100)
        if(b<0): b *= -1 
        if(b == 0): return 'error'

    return S

p = aproximace_pi(8)
print(p)
print(ma.pi)

#v = odmocnina(a**2 - (a/2)**2, 100)
#S = 6*a*(v/2)
#a = odmocnina((a/2)**2 + (1-v)**2,100)
import numpy as np
import math as ma

def odmocnina(a, n): #a = cislo #* n = pocet opakovani cyklu
    if(a == 0):
        return 0
    x=((a/a)+a)/2  
    for i in range(n):
        x = ((a/x)+x)/2 
    return x      


a = 554816
n = 50


x = odmocnina(a,n)
print(x)
print(ma.sqrt(a))
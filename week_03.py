import numpy as np

def prvocisla(n, prim = []):
    if(len(prim) != 0): N = max(prim)
    else: N = 2
    while 1:
        prvocislo_otaznik = True
        for i in range(2, N):
            if(N % i == 0):
                prvocislo_otaznik = False
                break
        
        if prvocislo_otaznik:
            prim.append(N)
            
        N += 1
        if(len(prim) == n): return prim
prim = prvocisla(10)
print(prim)

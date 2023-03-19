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
        S = 6*(b*(v/2))*(2**i)
        b = odmocnina((b/2)**2 + (1-v)**2,100) #max 97, pro vetsi pocet n-uhelniku je potreba vice iteraci
        if(b == 0): return 'error'
    return S

def aproximace_pi_newton(n):
    a = 1/16
    sum = 0
    for i in range(1,n+1):
        sum += (a/(2*i+1))
        a = a*((2*(i+1)-3)/(2*(i+1)*4))

    m = odmocnina(3,1000)
    q = 12*(-(m/8) + 1/2 - sum)
    return q
    
q = aproximace_pi_newton(100)
p = aproximace_pi(97)
print(q)
print('------------------')
print(p)
print('------------------')
print(ma.pi)
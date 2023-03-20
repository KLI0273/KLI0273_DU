def faktorial(N):
    sum = 1
    for i in range(1,N+1):
        sum = sum*i
    return sum

def rek_fact(n, sum):
    if(n == 0):
        return sum
    sum = sum * n
    return rek_fact(n-1, sum) 

def prumer(lis):
    sum = 0
    for i in range(len(lis)):
        sum += lis[i]
    return sum/len(lis)

def prvocisla(n):
    N,j = 2,0
    list_prv = list(range(n+1))
    
    while 1:
        prvocislo_otaznik = True
        for i in range(2, N):
            if(N % i == 0):
                prvocislo_otaznik = False
                break
        
        if prvocislo_otaznik:
            list_prv[j] = N
            j += 1
            
        N += 1
        if(list_prv[n] != n): return list_prv

f = faktorial(6)
print(f)
rf = rek_fact(6, 1)
print(rf)
lis = [1,2,3,4,5,6,7,8,9]
pr = prumer(lis)
print(pr)
prv = prvocisla(10)
print(prv)


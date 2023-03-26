#samostatne funkce jsou v test.py
# ukol 1-3 jsou v week_02.py

name = 'Marek'
vek = 20
cislo = 8.15

list = ['Marek', 20, 8.15]
touple = ('Marek', 20, 8.15)
dict = {0:'Marek', 1:20, 2:8.15}

for i in range(3):
    print(type(list[i]))

for i in range(3):
    print(id(list[i]))
    print(id(touple[i]))
    print(id(dict[i]))

print(id(name))
print(id(vek))
print(id(cislo))

name = 'Pepa'

print(id(name))
print(id(list[i]))
print(id(touple[i]))
print(id(dict[i]))

print(str(name), str(vek), str(cislo))

a1,b1 = 4, 5
a2,b2 = 4.5, 5.4
a3,b3 = str(3), str(4)
t,f = True, False

list1 = [a1, a2, t, a3 ]
list2 = [b1, b2, f, b3 ]
for i in range(4): #*par podminek pro ktere operace nemaji smysl
    print(list1[i] + list2[i])
    if(i != 3):print(list1[i] - list2[i])
    if(i != 3):print(list1[i] * list2[i])
    if(i != 2 | i != 3):print(list1[i] / list2[i])
    if(i != 2 | i != 3):print(list1[i] % list2[i])
    if(i != 3):print(list1[i] ** list2[i])
    if(i != 2 | i != 3):print(list1[i] // list2[i])

print(dir(touple))
print(dir(list))
print(dir(dict))
print(dir(name))
print(dir(vek))
print(dir(cislo))
print(dir(list1))
print(dir(list2))

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
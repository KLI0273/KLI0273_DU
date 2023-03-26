def gen_fibb():
    i1 = 0
    i2 = 1
    yield i1
    yield i2
    while True:
        f = i1 + i2
        yield f
        i1 = i2
        i2 = f  
fib = []
gfib = gen_fibb()
for i in range(10):
    fib.append(next(gfib))
print(fib)

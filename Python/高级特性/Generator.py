#斐波那契数列
def fib(max):
    n,a,b =  0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

for n in fib(6):
    print (n)

#要拿到函数返回值，必须捕获StopIteration错误
g = fib(6)
while True:
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        print ('Generator return value:',e.value)
        break
        
#杨辉三角
def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]

n=0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

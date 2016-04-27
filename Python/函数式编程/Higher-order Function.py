x = abs(-10)
print (x)

f = abs
print (f)

def add(x,y,f):
    return f(x)+f(y)

x = -5
y = 6
print (add(x,y,f))

#加入可变参数
from math import sqrt

def same(x,*fs):
    s=[f(x) for f in fs]
    return s

print(same(2,sqrt,abs))

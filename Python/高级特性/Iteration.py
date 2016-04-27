#--coding:utf-8-----

for ch in 'ABC':
    print (ch)

d = {'a':1,'b':2,'c':3}
for key in d:
    print(key,d[key])

#下标循环
for i,value in enumerate(['a','b','c']):
    print (i,value)


for x,y in [(1,1),(2,4),(3,9)]:
    print (x,y)


#判断一个对象是否可以迭代
from collections import Iterable

print (isinstance ([1,2,3],Iterable))
print (isinstance ('abc',Iterable))
print (isinstance (123,Iterable))

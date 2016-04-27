#--coding:utf-8----
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print (L[0:3])
print (L[:3])
print (L[1:3])
 
print (L[-2:])
print (L[-2:-1])

L = list(range(100))

print (L[:10])
print (L[-10:])
print (L[10:20])
print (L[:10:2])
print (L[::5])

#tuple也可以做切片操作，结果仍为切片
print ((0, 1, 2, 3, 4, 5)[:3])

#字符串也可以看成一种List
print ('ABCDEFG'[0:3])
print ('ABCDEFG'[0::2])
 
 
 

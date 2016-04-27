L = [x*x for x in range(1,11)]
print (L)

L = [x*x for x in range(1,11) if x%2==0]
print (L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print (L)

#列出当前目录下的文件名
import os
L = [d for d in os.listdir('.')]
print (L)


d = {'x': 'A', 'y': 'B', 'z': 'C' }
L = [k + '=' + v for k, v in d.items()]
print (L)


#字符串小写
L = ['Hello', 'World', 'IBM',18, 'Apple']
List = [s.lower() for s in L if isinstance(s,str)]
print (List)

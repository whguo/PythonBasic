def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print (list(r))

print (list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x,y):
    return 10*x+y

print (reduce(add,[1,3,5,7,9]))



#把字符串转换成数字
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print (str2int('21'))

#利用map()函数，把用户输入的不规范的英文名字，
#变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def fn(name):
    return name[0].upper()+name[1:].lower()

print (list(map(fn,['adam','LISA','barT'])))

#编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(l):
    return reduce(lambda x,y:x*y,l)

print (prod([1,3,5,7,9]))


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    pos = s.find('.')
    def fn(x, y):
        return x * 10 + y
    def fny(x, y):
        return x * 0.1 + y
    def char2num(l):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[l]
    return reduce(fn,map(char2num,s[0:pos]))+0.1*reduce(fny,map(char2num,s[pos+1:][::-1]))

print (str2float('123.4567'))

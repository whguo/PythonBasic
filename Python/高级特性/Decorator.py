#最简单函数，调用两次
def myfunc():
    print('myfunc() called.')

myfunc()
myfunc()
print('-----------------------------')

#使用装饰函数在函数执行前和执行后分别附加额外功能
def deco(func):
    print('before myfunc() called.')
    func()
    print('after myfunc() called.')
   # return func

def myfunc1():
    print('myfunc1() called.')

myfunc1 = deco(myfunc1)
myfunc1()
myfunc1()
print('-----------------------------')

#使用语法糖@来装饰函数
@deco
def myfunc2():
    print('myfunc() called.')

myfunc2()
myfunc2()

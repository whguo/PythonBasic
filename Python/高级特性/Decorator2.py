#使用内嵌包装函数来确保每次新函数都被调用
def deco(func):
    def _deco():
        print('before myfunc() called.')
        func()
        print('after myfunc() called.')
        #不需要返回func,实际上应该返回原函数的返回值
    return _deco

@deco
def myfunc():
    print('myfunc() is called.')

myfunc()
myfunc()

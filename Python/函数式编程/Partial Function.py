print(int('12345'))

print(int('12345',base=8))

print(int('12345',16))

#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，
#于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去
def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))
print(int2('1010101'))


##########################################
import functools
int8 = functools.partial(int,base=8)
print(int8('1000'))
print(int8('1010'))

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（设置默认值）
#返回一个新的函数，调用这个新函数会更简单

#注意到上面的新的int8函数，仅仅是把base参数重新设定默认值为8，
#但也可以在函数调用时传入其他值
print(int8('100001',base=2))

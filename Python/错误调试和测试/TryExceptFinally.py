try:
    print('try...')
    #r = 10/int('2')
    #r = 10/0
    r = 10/int('a')
    print('result',r)
except ValueError as e:
    print ('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END----------------------------------')


#另一种处理方式
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!',e)
        raise   #raise语句如果不带参数，就会把当前错误原样抛出

bar()
#在bar()函数中，我们明明已经捕获了错误，但是，
#打印一个ValueError!后，又把错误通过raise语句抛出去了
#捕获错误目的只是记录一下，便于后续追踪。
#但是，由于当前函数不知道应该怎么处理该错误，
#所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
#好比一个员工处理不了一个问题时，就把问题抛给他的老板，
#如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

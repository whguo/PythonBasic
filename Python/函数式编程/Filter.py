#求序列中奇数
def is_odd(n):
    return n%2 == 1

L = list(filter(is_odd,[1,2,4,5,6,9,10,15]))
print (L)

#删除序列中的空字符串
def not_empty(s):
    return s and s.strip()  #这里注意and用法

L = list(filter(not_empty,['A',' ',' B',None,'C ','  ','']))
print (L)


#用filter求素数：埃氏筛法

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = _odd_iter()   #初始序列
    while True:
        n = next(it)    #返回序列第一个数
        yield n
        it = filter(_not_divisible(n),it)   #把能整除的去掉，构造新序列

#1000以内的素数
for n in primes():
    if n<1000:
        print (n)
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
#请利用filter()滤掉非回数：
def is_palindrome(n):
    a = str(n)
    return a==a[::-1]
    
output = filter(is_palindrome, range(1, 1000))
print(list(output))

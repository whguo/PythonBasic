#类型判断函数type
print(type(123))
print(type('123'))
print(type(None))

print(type(abs))


#isinstance()函数在判断继承关系时更好用
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h,Husky))
print(isinstance(h,Dog))
print(isinstance(h,Animal))
print(isinstance(h,Animal) and isinstance(d,Animal))

print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

#判断是某些类型中的一种
print(isinstance('a',(int,str,bytes)))
print(isinstance('a',(int,bytes)))
print(isinstance([1,2,3],(list,tuple)))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('ABC'))

#getattr()、setattr()以及hasattr()，可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
         self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()
if hasattr(obj,'x'):
    print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',10)
if hasattr(obj,'y'):
    print(obj.y)
print(getattr(obj,'y'))

#可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj,'z',404))

print(hasattr(obj,'power'))
print(getattr(obj,'power'))

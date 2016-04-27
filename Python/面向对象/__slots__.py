class Student(object):
    pass

#给实例绑定属性
s = Student()
s.name = 'Michael'
print(s.name)

#给实例绑定方法
def set_age(self,age):
    self.age=age

from types import MethodType

s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

#给一个实例绑定的方法对另一个实例是不起作用的
s2 = Student()
#s2.set_age(22)

#要让所有实例都能用该方法，可以给该class绑定方法
def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,Student)
s.set_score(100)
s2.set_score(99)

#属性分实例属性和类属性，多个实例同时更改类属性，值是最后更改的一个
print(s.score,s2.score)
#由于s和s2自身没有score属性，所以打印的是类属性score的值

s.score = 101
s2.score = 90
print(s.score,s2.score)
#这两个分别是实例s和s2自身的属性，仅仅是与类属性score同名，并没有任何关系

#使用__slots__限制实例属性
class Worker(object):
    __slots__ = ('name','age')

w = Worker()
w.name = 'Michael'
w.age = 22
w.money = 4534
#money没有被放到__slots__中，所以不能绑定该属性
#注意__slots__只对当前类的实例起作用，对继承子类的属性不起作用
#除非在子类中也相应的使用__slots__


#tips:
# slots只能限制添加属性，不能限制通过添加方法来添加属性

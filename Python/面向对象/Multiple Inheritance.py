#多重继承
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass


#为了不让类的数量持续增多，不再分能飞和不能飞的哺乳动物类，
#只需先定义Runnalbe和Flyable类

class Runnalbe(object):
    def run(slef):
        print('Running....')

class Flyable(object):
    def fly(slef):
        print('Flying....')

class Dog(Mammal,Runnalbe):
    pass

class Bat(Mammal,Flyable):
    pass

d = Dog()
d.run()
b = Bat()
b.fly()

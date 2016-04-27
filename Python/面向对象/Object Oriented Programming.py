class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()

#允许对实例变量绑定任何数据，也就是同一类的实例拥有的变量可能不一样
bart.age=8
print(bart.age)

#不存在
print(lisa.age)

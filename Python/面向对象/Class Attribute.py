#有时类本身也需要一个属性：类属性
class Student(object):
    stuNum = 0
    name = 'Student'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print(s.name)
print(s.score)

#类属性
print(Student.stuNum)
print(Student.name)

s.name = 'Michael'
print(s.name)

del s.name
print(s.name)
#不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性
#但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性


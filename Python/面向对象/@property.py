#普通的get和set方法
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an intager!')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

#s.set_score(a)
#s.set_score(999)
print('-------------------------------')

#使用@property装饰器责把一个方法变成属性调用
class Worker(object):
    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self,value):
        if not isinstance(value,int):
            raise ValueError('wage must be an intager!')
        if value<0 :
            raise ValueError('wage must bigger than zero')
        self._wage = value
        
#把一个getter方法变成属性，只需要加上@property就可以了，
#此时,@property本身又创建了另一个装饰器@score.setter，
#负责把一个setter方法变成属性赋值
w = Worker()
w.wage = 1000  # OK，实际转化为s.set_wage(1000)
print(w.wage)  # OK，实际转化为s.get_wage()
#w.wage = 'a'
#w.wage = -1
print('-------------------------------')


#定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
class Teacher(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2016-self._birth

t = Teacher()
t.birth = 1993
print(t.age)
#上面的birth是可读写属性，而age就是一个只读属性，
#因为age可以根据birth和当前时间计算出来



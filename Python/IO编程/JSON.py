#把python对象序列化为JSON
import json
d = dict(name='Bob',age=20,score=80)
print(json.dumps(d))

#把JSON反序列化为Python对象
json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str))


#把任意一个对象序列化
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob',20,99)
#不能直接序列化，是因为默认情况下，
#dumps()方法不知道如何将Student实例变为一个JSON的{}对象
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score}
print(json.dumps(s,default = student2dict))

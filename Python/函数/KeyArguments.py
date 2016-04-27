def person(name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)

person('Bob',35,city='beijing')
person('Adam',33,gender='M',job='Engineer')

kw = {'city':'taiyuan','job':'chengxuyuan'}
person('jack',24,**kw)


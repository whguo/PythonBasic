#在内存中读写str

#写
from io import StringIO

f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())
print('--------------------------------------')

#读
ff = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = ff.readline()
    if(s==''):
        break
    print(s.strip())
print('--------------------------------------')

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#BytesIO实现了在内存中读写bytes
from io import BytesIO
f = BytesIO()
print(f.write('中文'.encode('utf-8')))
print(f.getvalue())



#StringIO不需要close，需要close()的stream也不建议手动close，而是用with自动close

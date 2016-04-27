import os
print(os.name)
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print('-------------------------------------------------------------------------')


#环境变量
print(os.environ)
#某个环境变量
print(os.environ.get('PATH'))
print('-------------------------------------------------------------------------')
print(os.environ.get('x','default'))
print('-------------------------------------------------------------------------')

#操作文件和目录
#查看当前目录的绝对路径
print(os.path.abspath('.'))

#在某个目录下创建一个新的目录，首先把新目录的完整路径表示出来
dire = os.path.join(os.path.abspath('.'),'testdir')
print(dire)
os.mkdir(dire)
print('-------------------------------------------------------------------------')
os.rmdir(dire)

#把两个路径合成一个时，不要直接拼字符串，
#而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
#这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split(dire))

#os.path.splitext()可以直接得到文件扩展名
print(os.path.splitext('F:\\郭维汉\\Python\\IO编程\\test.txt'))
#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

#对文件重命名
f = open('test2.txt','w')
f.write('Hello!')
f.close()
os.rename('test2.txt','test1.txt')
os.remove('test1.txt')

#列出当前目录所有文件
file = [x for x in os.listdir('.')]
print(file)
print('-------------------------------------------------------------------------')
#列出所有的.py文件
file = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(file)

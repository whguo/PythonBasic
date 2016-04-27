f = open('./test.txt','r')
str = f.read()
print(str)
print('--------------------------------------------')
f.close()

#增加错误处理
try:
    f = open('./test.tx','r')
    print(f.read())
except:
    print('No such file!')
finally:
    if f:
        f.close()
print('--------------------------------------------')
#更简便的写法，用with
with open('./test.txt','r') as f:
    print(f.read())
#不用写close
print('--------------------------------------------')
#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，
#所以，要保险起见，可以反复调用read(size)方法，
#每次最多读取size个字节的内容。

#另外，调用readline()可以每次读取一行内容，
#调用readlines()一次读取所有内容并按行返回list。

#如果文件很小，read()一次性读取最方便；
#如果不能确定文件大小，反复调用read(size)比较保险；
#如果是配置文件，调用readlines()最方便：
f = open('./test.txt','r')
for line in f.readlines():
    print(line.strip()+'...')  #把末尾的\n去掉

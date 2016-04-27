#二进制文件
#f = open('./test.jpg','rb')
#print(f.read())

#字符编码
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
f = open('./gbk.txt','r',encoding='gbk')
print(f.read())

#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
#因为在文本文件中可能夹杂了一些非法编码的字符。
#遇到这种情况，open()函数还接收一个errors参数，
#表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
f = open('./gbk.txt', 'r', encoding='gbk', errors='ignore')


#写文件
f = open('./test.txt','w')
f.write('Hello,World!\n')
f.write('HaHa!\n')
f.write('WOW\n')
f.close()

#忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
#所以，还是用with语句来得保险
#with open('./test.txt', 'w') as f:
#    f.write('Hello, world!')
#使用with语句操作文件IO是个好习惯

#序列化
#序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
#反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

import pickle
d = dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()

ff = open('dump.txt','rb')
dd = pickle.load(ff)
ff.close
print(dd)

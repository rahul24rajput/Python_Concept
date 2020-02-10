import os
os.chdir('D:/Rahul/Grpah_with_frequency/')

f=open('test1.txt','r')
m=open('test2.txt','a')

for each in f:
    if ':' in each:
        m.write(each)
    else:
        pass
    
m.close()
f.close()

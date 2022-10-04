a= open('reversedtext1.txt','w+')
f=open('text1.txt','r')
for i in f.readlines():
    a.write(str(i)[::-1])
a.close()
f.close()
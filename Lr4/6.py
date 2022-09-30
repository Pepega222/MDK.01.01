a=[1,2,3,4,5,6,7,8,9,10,20,30,40]
for i in a:
    if i%2 ==0:
        print(i)
    elif str(i).endswith('0'):
        print(i)
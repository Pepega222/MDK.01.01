a=[int(i) for i in range(1,10001)]
b=[]
for i in range(len(a)):
    if (a[i] % 7 == 0 and a[i] % 3 == 0) or a[i] % 9 :
        b.append(a[i])
print(b)
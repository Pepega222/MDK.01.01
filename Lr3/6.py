a=[int(i) for i in range(-10, 11)]
s=0
for j in range(len(a)):
    while a[j] < 0 :
        j+=1
        s+=1
    break
print("Кол-во отриц чисел:", s)
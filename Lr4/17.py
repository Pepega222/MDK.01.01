a=[[1,10], [2, 20], [3, 30], [4, 40]]
b=[]
for i in range(len(a)):
    for j in a[i]:
        b.append(j)
print(b)
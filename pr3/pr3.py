a=[1,4,2,5,6,8,3,7,10,15,11]
for i in range(len(a)):  
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
#Сложность алгоритма O(n^2)

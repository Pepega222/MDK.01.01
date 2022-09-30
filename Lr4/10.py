l=[1,2,3,4,5,6,7,8,9,10]
k1,k2= int(input("Позиция ")), int(input("Позиция "))
print(l[k2:] + l[k1:k2] + l[:k1])

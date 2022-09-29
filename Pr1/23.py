m1=[1,2,3,4,5,6,7,8,9,10]
m2=[1,2,3,79,764,324,12,4,8,19]
m3=[]
for j in range(len(m2)):
    if m2[j] not in m1:
        m3.append(m2[j])
print(m3)


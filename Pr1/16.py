a=['Светлана','Анастасия','Оля','Маша','Анастасия','Оля','Маша','Светлана']
groups=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i!= j:
            groups+=1
print('Количество пар: ', groups//2)


a=[]
n=float(input("Введите курс доллара: "))
for i in range(1,21):
    a.append(i*n)
print(*a , sep='; ')
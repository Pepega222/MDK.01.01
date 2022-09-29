a,b=int(input()), int(input())
s=0
for i in range(a, b+1):
    s+=i**2
print("Сумма квадратов целых чисел от", a,"до", b, "равна", s)

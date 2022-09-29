from math import factorial

n=int(input('Введите n:1<n<=10 ' ))
summ = 0
for i in range(n+1):
    summ+= factorial(i)
print(summ)


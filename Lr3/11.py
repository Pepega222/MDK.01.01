from math import *
f = int(input("Введите факториал числа n: "))
for n in range(1,f+1):
    if factorial(n) == f:
        print("Число n =",n)
        break
    
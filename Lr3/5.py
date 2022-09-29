from math import *
n=int(input())
s=0
for i in range(1,n+1):
    s+=factorial(i)
    s+=i
print(s)
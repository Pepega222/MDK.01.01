from math import *
def function(x):
    f = x**2-4
    return f
def Bisection(a, b, e):
    while (b-a) > e:
        c = (a+b)/2
        f_a = function(a)
        f_b = function(b)
        f_c = function(c)
        if f_a*f_c > 0:
            a = c
        else:
            b = c
    return ((a+b)/2)
A = -10
B = 10
E = 10**(-15)
print (Bisection(A, B, E))
def function(x):
 f = x**2-4
 return f
def Bisection(a, b, e):
    n = 0
    while (b-a) > e:
        n = n + 1
        c = (a+b)/2
        f_a = function(a)
        f_b = function(b)
        f_c = function(c)
        if f_a*f_c > 0:
            a = c
        else :
            b = c
    return ((a+b)/2, n)
A = -10
B = 10
E = 10**(-15)
print(Bisection(A, B, E))

def summa(a,b):
    c = a + b
    return c
num1 = int (input ())
num2 = int (input ())
summa(num1 , num2)




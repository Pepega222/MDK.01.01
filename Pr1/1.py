from math import sin

x=int(input('введите значение x '))
if x >0:
    print('y=', sin(x**2))
else:
    print('y=', 1+2*(sin(x)**2))
from math import *
def f(x,y):
    print('z1 = ', sin(x+0.5) - y - 1 )
    print('z2 = ', x + cos(y-2))
    quit()
print(f(x=int(input()), y=int(input())))
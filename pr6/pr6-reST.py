n=int(input("Введите целое число, больше 1 ")) 
def number(n):
    """
This is a reST style.

:param n:  целое число, которое проверяется, просто оно или составное
:returns: n, "имеет делитель" , d Если число составное.  n, "простое число" Если число простое
:raises keyError: n не число или null
    """
    for d in range(2, n):           
        if n % d == 0:                        
            print (n, "имеет делитель", d )     
            break                             
        else:                                     
            print (n, "простое число" )
            break 
print(number(n))            
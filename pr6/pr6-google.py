n=int(input("Введите целое число, больше 1 ")) 
def number(n):
    """Определение, является ли число простом или составным

    Args:
        n (int): Число, которое нужно проверить

    Returns:
        str: возвращает число, "имеет делитель", делитель Если число составное
        str: возвращает число, "простое число"  Если простое
    """ 
    for d in range(2, n):         
        if n % d == 0:                        
            print (n, "имеет делитель", d )     
            break                             
        else:                                     
            print (n, "простое число" )
            break     
print(number(n))        
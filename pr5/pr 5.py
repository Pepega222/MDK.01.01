def fac(n): #Сложность алгоритма равна O(log n)       
    if n == 0:
        return 1
    return fac(n-1) * n
print(fac(23))
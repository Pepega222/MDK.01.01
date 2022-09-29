a,b, c= int(input()), int(input()), int(input())

print('каждое из чисел А и В больше 100 ')
print()
if a >100 and b >100:
    print("Условие истинно")
else:
    print("Условие не истинно")
print()
print('только одно из чисел А и В четное')
print()
if a%2 == 0 or b%2 == 0:
    print("Условие истинно")
else:
    print("Условие не истинно")
print()
print('хотя бы одно из чисел А и В положительно')
print()
if a>0 or b>0 :
    print("Условие истинно")
else:
    print("Условие не истинно")
print()
print('каждое из чисел А, В, С кратно трем')
print()
if a%3 == 0 and  b%3 ==  0 and c%3 == 0:
    print("Условие истинно")
else:
    print("Условие не истинно")
print()
print('только одно из чисел А, В и С меньше 50')
print()
if a <50 or  b<50 or c<50:
    print("Условие истинно")
else:
    print("Условие не истинно")
print()
print('хотя бы одно из чисел А, В, С отрицательно')
print()
if a <0 or  b<0 or c<0:
    print("Условие истинно")
else:
    print("Условие не истинно")

Digit=input('Введите число:\n')
Spisok_Digit=list(Digit)
 
Max_Digit=max(Spisok_Digit) #максимальное число
Min_Digit=min(Spisok_Digit) #минимальное число
 
print('Максимальная цифра =', Max_Digit)
print('Минимальная цифра =', Min_Digit)
 
Poz1=Spisok_Digit.index(Max_Digit) #позиция макс. цифры
Poz2=Spisok_Digit.index(Min_Digit) #позиция мин. цифры
 
if Poz1<Poz2:
    print('Левее расположена максимальная цифра =', Max_Digit)
else:
    print('Левее расположена минимальная цифра =', Min_Digit )

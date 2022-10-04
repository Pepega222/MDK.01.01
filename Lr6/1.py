a=list(input("Введите числа"))
for i in range(len(a)):
    print("Цифра", a[i], "встречается", a.count(a[i]), "раз(а)")
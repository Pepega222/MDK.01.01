a=list(input("Введите первый список чисел "))
b=list(input("Введите первый список чисел "))
c = list(set(a) & set(b))
for i in c:
    print("Число:",i,"встречается в двух списках",a.count(i)+b.count(i),"раз(а)")
a=[1,2,3,4,5]
def search(a, key):
    for i in range(len(a)):
        if a[i] == key:
            return ("Число:",key,"есть в списке")
    return ("Числа:",key,"нет в списке")
print(search(a,5))
#Сложность алгоритма - O(n)

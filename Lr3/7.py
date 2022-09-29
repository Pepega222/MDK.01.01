a=[1,1]
for i in range(11):
    a.append(a[i]+a[i+1])
n=int(input())
for i in a:
    if n < i:
        print('Последовательность Фибоначи', *a )
        print('Первое число, большее',n, 'это',i)
        break
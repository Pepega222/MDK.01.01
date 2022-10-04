a = open("text1.txt", "r")
max=0
for i in a.readlines():
    if len(i) > max:
        max = len(i)
        maxx=i
print('Длина самой длиной строки: ',max)
f = open("text1.txt", "r")
print('номер самой длинной строки: ',f.readlines().index(maxx))
print('Самая длинная строка:',maxx)
names = ['Маша', 'Петя', 'Вася']
for i in range(len(names)):
    names[i] = hash(names[i])
print(names) 
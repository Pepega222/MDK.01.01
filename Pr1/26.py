
text='Шварценеггер все так же молча смотрел на нее и улыбался Мария потупилась и покраснела и тогда Шварценеггер ласковым но непреодолимо сильным движением развернул ее и повел рядом с собой'
text=text.split()
a={}
for i in text:
    a[i] = text.count(i)
sorted_values = sorted(a.values()) # Sort the values
sorted_dict = {}
for i in sorted_values:
    for k in a.keys():
        if a[k] == i:
            sorted_dict[k] = a[k]
            break
print(sorted_dict)
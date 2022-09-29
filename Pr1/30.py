s='''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated'''
print('''Кол-во букв: ''', sum(map(str.isalpha,s)))
print('''Кол-во слов: ''', len(s.split()))
print('''Кол-во строк: ''', len(s.split('\n')))


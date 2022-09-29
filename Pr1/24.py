text='Дан текст, состоящий из строк. Определить количество слов в тексте.'
text=text.replace(',','')
text=text.split()
print('Слов: ',len(text))


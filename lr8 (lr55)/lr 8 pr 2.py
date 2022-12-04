import re

txt = "Arthur is 18 years old, his father, Aleksei, is 54.\
 His grandfather Janos was born at the start of WW-2 in 1942.\
 He was 77 years old when he died in 2018"
'''
Поскольку указанный в тексте возраст состоит из 2 или 3 цифр, то
используется регулярное выражение \d{2,3}. Оно с двух сторон ограничено \b,
поскольку нам не нужны группы из 2 или 3 цифр, полученные из числа 1942.
С именами в данном тексте все просто. Вполне сработает поиск всех слов,
начинающихся с заглавных букв и содержащих более 3 символов. Делаем это также
с границами.
'''
ages = re.findall(r'\b\d{2,3}\b', txt)
names = re.findall (r'\b[A-Z][a-z]{3,}\b',txt)
print(dict(zip(names, ages)))

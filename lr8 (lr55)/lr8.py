# Импортируем библиотеки
import re
'''
В данном примере рассматривается обобщенный шаблон e-mail:
someone@mailservice.domain
'''
# Определяем допустимые шаблоны ввода электронной почты
pattern_email = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|org|edu)"
#Создаем поле для ввода адреса электронной почты
user_input = input()
if (re.search(pattern_email, user_input)):
 print(f"{user_input} is a valid email.")
else:
 print(f"{user_input} is invalid.")
# Импортируем библиотеки
import getpass
import re
pattern_password =\
r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Zaz\d@$!%*?&]{8,}$"
# Используем getpass вместо стандартной функции ввода
# Это позволит скрыть запись как в реальной жизни
user_input = input("Password: ")
invalid_pass_text = \
"Your password must have at least 8 characters,\
at least an upper case letter,\
a lowercase letter, a number, \
and a symbol so as to be secure"

if (re.search(pattern_password, user_input)):
    print("Strong Password Set")
else:
    print(invalid_pass_text)

# https://docs.python.org/3.11/library/stdtypes.html#string-methods
# https://www.w3schools.com/python/python_ref_string.asp

'''
len(str) - Длина строки
str.format(*args, **kwargs) - Форматирование строки

str.capitalize() - Возвращает копию строки с первым символом заглавной буквой и остальными строчными буквами.

str.casefold() - Преобразует строку в нижний регистр
str.lower() - Преобразует строку в нижний регистр

str.center(width[, fillchar]) - Возвращает отцентрованную строку, по краям которой стоит символ fillchar (по умолчанию пробел)

str.count(sub[, start[, end]]) - Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)

str.find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
str.index(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError

str.replace(шаблон, замена) - Замена шаблона

str.split([символ])- Разбиение строки по разделителю

str.isdigit() - Состоит ли строка из цифр
str.isalpha() - Состоит ли строка из букв
str.isalnum() - Состоит ли строка из цифр или букв
str.islower() - Состоит ли строка из символов в нижнем регистре
str.isupper() - Состоит ли строка из символов в верхнем регистре
'''

# s = 'привет, мир!'
# print(s.capitalize())

# s = 'ПРИВЕТ, МИР!'
# print(s.casefold())

# s = 'ПРИВЕТ, МИР!'
# print(s.center(20, '!'))

# s = 'Home, sweet Home'
# print(s.count('Home', 0, 10))

# s = 'Home, sweet Home'
# print(s.index('ee'))

s = 'Home, sweet Home'
print(s)
s = s.replace('Home', 'home', 1)
print(s)

# i = 1
# while i <= 10:
#     print(i, end=' ')
#     i += 1

# i = 10
# while i > 0:
#     print(i, end=' ')
#     i -= 1

# i = 0
# while i < 11:
#     i += 1
#     if i == 4:
#         continue
#     if i == 8:
#         break
#     print(i, end=' ')

# i = 1
# while i < 11:
#     print(i, end=' ')
#     i += 1
# else:
#     print('Oops')

# age = int(input('Сколько вам лет? '))
# while age < 18 or age > 65:
#     print('Возраст не подходит')
#     age = int(input('Сколько вам лет? '))
# else:
#     print('Добро пожаловать!')

# age = int(input('Сколько вам лет? '))
# while age < 18 or age > 65:
#     if age < 18:
#         print('Вы слишком молоды')
#     elif 65 < age <= 100:
#         print('Вам уже сюда не нужно')
#     elif age > 100:
#         print('Вы точно не ошиблись с возрастом?')
#     age = int(input('Сколько вам лет? '))
# else:
#     print('Добро пожаловать!')

# while True:
#     age = int(input('Сколько вам лет? '))
#     if age < 18:
#         print('Вы слишком молоды')
#     elif 65 < age <= 100:
#         print('Вам уже сюда не нужно')
#     elif age > 100:
#         print('Вы точно не ошиблись с возрастом?')
#     else:
#         print('Добро пожаловать!')
#         break

# Homework
'''
Напишите 4 решения для вывода в цикле while четных и нечетных чисел от 0 до 10 вкобчительно
Два условия - для вывода четных чисел и два условия - для вывода нечетных
'''
i = 0
while i <= 10:
    # i % 2 == 0
    # not i % 2
    # i % 2 != 0
    # i % 2
    if i % 2:
        print(i, end=' ')
    i += 1

'''
Дана строка: s = 'Hello world'
В цикле выведите посимвольно данную строку. Попробуйте написать 2 решения задачи, одно из которых будет использовать срезы.
'''
s = 'Hello world'
i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
while i < len(s):
    print(s[i:i + 1])
    i += 1

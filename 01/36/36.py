'''
При работе со списком часто требуется преобразовать элементы списка и вернуть новый список.
Для этого можно использовать цикл или генератор.
'''
list1 = [1, 2, 3]
# list1 = [x * 2 for x in list1]
# for i, el in enumerate(list1):
#     list1[i] = el * 2
# print(list1)

'''
Python предлагает более удобный способ решения такого рода задач с помощью встроенной функции map().
iterator = map(fn, list)
На самом деле вы можете передать в функцию map() любой итерируемый объект, а не только список или кортеж.
'''


def get_double(x):
    return x * 2


# list1 = list(map(get_double, list1))
list1 = list(map(lambda x: x * 2, list1))
print(list1)

'''
Иногда вам нужно перебрать элементы списка и выбрать некоторые из них на основе заданных критериев.
'''
list1 = list(range(1, 11))
# list1 = [x for x in list1 if x % 2 == 0]

'''
В Python есть встроенная функция filter(), которая позволяет более красиво фильтровать список (или кортеж).
filter(fn, list)
Функция filter() перебирает элементы списка и применяет функцию fn() к каждому элементу. Он возвращает итератор для элементов, где функция fn() возвращает True.
'''


def get_even(num):
    return num % 2 == 0


# list1 = list(filter(get_even, list1))
list1 = list(filter(lambda num: num % 2 == 0, list1))
print(list1)

'''
Функция zip() принимает итерации (может быть ноль или больше), объединяет их в кортеж и возвращает его.
'''
num_list = [1, 2, 3, 4, 5]
str_list = ['one', 'two', 'three']
res_list = list(zip(num_list, str_list))
res_dict = dict(zip(str_list, num_list))
print(res_list)
print(res_dict)

# unzip
a, b = zip(*res_list)
print(a)
print(b)

c = list(zip(*res_dict.items()))
d = list(zip(*res_dict))
print(c)
print(d)

# Homework
'''
Даны коллекции элементов:
['david', 'peter', 'jenifer']
('paris', 'minsk', 'mexico')
Напишите несколько решений, чтобы привести первую букву каждого элемента к верхнему регистру.
['David', 'Peter', 'Jenifer']
('Paris', 'Minsk', 'Mexico')
Решения оформите в виде пользовательской функции. Функция по умолчанию должна возвращать список. По требованию - кортеж.
'''


# def set_capitalize(lst, tpl=False):
#     if tpl:
#         return tuple(el.capitalize() for el in lst)
#     else:
#         return [el.capitalize() for el in lst]


def set_capitalize(lst, tpl=False):
    if tpl:
        return tuple(map(lambda el: el.capitalize(), lst))
    else:
        return list(map(lambda el: el.capitalize(), lst))


print(set_capitalize(['david', 'peter', 'jenifer']))
print(set_capitalize(('paris', 'minsk', 'mexico'), True))

'''
Дан список городов:
cities = [
    ['Mexico', 8_855_000],
    ['Paris', 2_161_000],
    ['Minsk', 1_975_000],
    ['Rio de Janeiro', 6_748_000],
    ['Tokio', 13_960_000],
]
Напишите несколько решений для получения списка городов с населением больше, чем передается параметром функции. Решение оформите в виде функции.
'''

cities = [
    ['Mexico', 8_855_000],
    ['Paris', 2_161_000],
    ['Minsk', 1_975_000],
    ['Rio de Janeiro', 6_748_000],
    ['Tokio', 13_960_000],
]
print(cities)


def get_cities(lst, min_population):
    return [i for i in lst if i[1] > min_population]


print(get_cities(cities, 2_000_000))


def get_cities(lst, min_population):
    def set_filter(i):
        return i[1] > min_population

    return list(filter(set_filter, lst))


print(get_cities(cities, 2_000_000))


def get_cities(lst, min_population):
    return list(filter(lambda i: i[1] > min_population, lst))


print(get_cities(cities, 2_000_000))

'''
https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BB%D0%B8%D0%BD%D0%B4%D1%80%D0%BE%D0%BC
Напишите функцию, которая будет получать параметром строку и возвращать True или False в зависимости от того, является ли строка палиндромом или нет.

топот  # True
saippuakivikauppias  # True
а роза упала на лапу Азора  # True
топот 2  # False
saippuakivikauppias 2  # False
а роза упала на лапу Азора 2  # False
'''


def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::-1]


print(is_palindrome('1212'))

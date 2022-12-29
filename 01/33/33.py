def greeting(say='Hello', name='Guest'):
    return f'{say}, {name}!'


# print()
print(greeting())
print(greeting('Hi', 'John'))
print(greeting('Good day'))
print(greeting('Good day'))

'''
Обязательные параметры должны стоять перед параметрами по умолчанию.
Именованные (ключевые) аргументы можно передвать в любом порядке. Пример с print
Использовав именованный аргумент, необходимо использовать по имени и все прочие аргументы. Позиционные аргументы после именованных не допускаются как при объявлении, так и при вызове.
'''


# def greeting(say='Hello', name):
#     return f'{say}, {name}!'

def greeting(name, say='Hello'):
    return f'{say}, {name}!'


print(greeting('Jack'))
print(greeting('Jack', 'Hi'))


def get_sum(a, b, c=1, d=0):
    return a + b + c + d


print(get_sum(5, 7))
print(get_sum(5, 7, d=10, c=20))
print(get_sum(5, 7, d=10))
# print(get_sum(5, 7, 10, c=20))  # error
# print(get_sum(5, 7, d=10, 20))  # error
print(get_sum(5, 7, 10, 20))


def get_sum(x, y, *args, mult=2, **kwargs):
    print(x)
    print(y)
    print(args)
    print(mult)
    print(kwargs)


get_sum(1, 2, 3, 4, mult=3, a=5, b=6, c=7)

# Python 3.8 - новый синтаксис параметров функции
# все, что находится перед / — строго позиционные аргументы, а все, что после * — только ключевые слова.


def my_func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)


# функцию можно вызвать как с позиционными, так и с именованными аргументами
my_func(1, 2, 3, 4, 5, 6)
my_func(a=1, b=2, c=3, d=4, e=5, f=6)


# и автор функции не сможем при необходимости изменить имя параметра, чтобы не потерялась совместимость
def my_func(a1, b, c, d, e, f):
    print(a1, b, c, d, e, f)


# my_func(a=1, b=2, c=3, d=4, e=5, f=6)  # error
my_func(a1=1, b=2, c=3, d=4, e=5, f=6)


def my_func(a1, b, /, c, d, *, e, f):
    print(a1, b, c, d, e, f)


# my_func(a1=1, b=2, c=3, d=4, e=5, f=6)  # error
# my_func(1, 2, 3, 4, 5, 6)  # error
my_func(1, 2, 3, 4, f=5, e=6)
my_func(1, 2, c=3, d=4, f=5, e=6)

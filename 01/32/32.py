'''
Функция — это именованный блок кода, который выполняет какую-то задачу и возвращат значение.
Функции нужны для того, чтобы избежать дублирования кода. В функцию можно обернуть код, который может потребоваться выполнить более одного раза и в нужных местах программы вызывать функцию.
print(), sum(), len()...
На практике функции создаются даже в тех случаях, если их используют только единожды, поскольку функции позволяют структурировать код, позволяют разделить большую программу на мелкие и более управляемые части кода.
'''


# hi()


def hi():
    """Printing Hello World."""
    print('Hello, World!')


# def hi2():
#     """Cool function
#
#     maybe."""
#     pass


hi()
# hi()
# hi()
# hi()
# hi()
# hi2()
# print('Hello, World!')
# print('Hello, World!')
# print('Hello, World!')
# print('Hello, World!')
# print('Hello, World!')

'''
Параметр — это часть информации, которая требуется функции. И вы указываете параметр в определении функции.
Аргумент — это часть данных, которую вы передаете в функцию.
'''


def hi(name):
    """Greeting."""
    print(f'Hello, {name}')


# print(type(hi))
hi('John')
hi('Jack')


def hi(name, greet):
    """Greeting."""
    print(f'{greet}, {name}!')


hi('John', 'Hi')
hi('John', 'Hello')
user = 'Jack'
say = 'Good day'
hi(user, say)


def get_sum(a, b):
    return a + b


print(get_sum(10, 20))
print(get_sum(101, 20))


def multiplication_table(x, y):
    """The function prints the multiplication table"""
    for i in range(1, x):
        for k in range(2, y):
            print(f'{i} * {k} = {i * k}\t', end='')
        print()
    else:
        print('Well done')


multiplication_table(10, 10)

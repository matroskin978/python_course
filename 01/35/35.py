a = 'global'


def fn():
    # a += '!'  # only read
    # a = 'local'
    global a
    a += '!'
    print(a)


print(a)
fn()
print(a)

print('*' * 30)

'''
Лямбда-функции в Python являются анонимными. Это означает, что функция безымянна. Как известно, ключевое слов def используется в Python для определения обычной функции. В свою очередь, ключевое слово lambda используется для определения анонимной функции.
lambda аргументы: выражение
'''


def get_double(x):
    return x ** 2


print(get_double(10))

get_double2 = lambda x: x ** 2
print(get_double2(10))

'''
Эта функция может иметь любое количество аргументов, но вычисляет и возвращает только одно значение. Синтаксически лямбда-функция ограничена, позволяет представить всего одно выражение.
Лямбда-функции используют вместе с такими встроенными функциями как filter(), map(),reduce() и др.
'''


def max_num(x, y):
    return x if x > y else y


print(max_num(7, 5))

# в лямбда-функции можно добавлять условие

max_num2 = lambda x, y: x if x > y else y
print(max_num2(7, 5))

print((lambda x, y: x if x > y else y)(7, 5))
res = (lambda x, y: x if x > y else y)(7, 14)
print(res)

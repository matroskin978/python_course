# функцию можно передавать в качестве параметра

def fn1():
    print('Hello from function fn1')


def fn2(func):
    print('Hello from function fn2')
    func()


fn2(fn1)


# также функцию можно присвоить переменной
def fn1():
    print('Hello from function fn1')


f = fn1
f()

'''
Суть декоратора заключается в том, что мы можем передать функцию в виде параметра другой функции. Эта другая функция и называется декоратором, декорирующей функцией.
'''


# рассмотрим пример самой идеи декоратора
def my_decorator(func):
    def wrapper():
        print('Before function')
        func()
        print('After function')

    return wrapper


@my_decorator
def fn_test():
    print('Hello from fn_test')


# мы обернули условную функцию func в обертку (декорировали ее). При этом результат работы этой функции не будет выводиться просто так, он будет возвращен и его можно при необходимости вызвать.
test_fn = my_decorator(fn_test)  # декорируем функцию
test_fn()  # вызываем декорированную функцию

fn_test()


# практический пример декоратора
def title_capitalize(fn):
    def wrapper():
        title = fn()
        title = title.capitalize()
        return title

    return wrapper


def add_dot(fn):
    def wrapper():
        title = fn()
        if not title.endswith('.'):
            title += '.'
        return title

    return wrapper


@add_dot
@title_capitalize
def hello():
    return 'hello, world'


print(hello())


# добавим аргумент
def title_capitalize(fn):
    def wrapper(s):
        title = fn(s)
        title = title.capitalize()
        return title

    return wrapper


def add_dot(fn):
    def wrapper(s):
        title = fn(s)
        if not title.endswith('.'):
            title += '.'
        return title

    return wrapper


@add_dot
@title_capitalize
def hello(s):
    return s


print(hello('hello, world'))
print(hello('hello, world.'))
print(hello('Hello, world.'))


# и переменное кол-во аргументов
def title_capitalize(fn):
    def wrapper(*args, **kwargs):
        title = fn(*args, **kwargs)
        title = title.capitalize()
        return title

    return wrapper


def end_symbol(fn):
    def wrapper(*args, **kwargs):
        title = fn(*args, **kwargs)
        end_s = kwargs['end'] if 'end' in kwargs else '.'
        title = title.rstrip(end_s)
        title += end_s
        return title

    return wrapper


@title_capitalize
@end_symbol
def hello(s, end='.'):
    return s + end


print(hello('hello, world!!!!!!', end='!'))
print(hello('hello, world!!!', end='?'))
print(hello('hello, world', end='!'))
print(hello('hello, world'))


@end_symbol
@title_capitalize
def hi():
    return 'hi test'


print(hi())

'''
Замыкание (closure) — функция, которая находится внутри другой функции и ссылается на переменные объявленные в теле внешней функции (свободные переменные).
'''

# def fn_outer(param):
#     def fn_inner():
#         print(param)
#
#     fn_inner()
#
#
# fn_outer('Test')


# def fn_outer(param):
#     def fn_inner():
#         print(param)
#
#     return fn_inner
#
#
# f = fn_outer('Test1')
# f()
# fn_outer('Test2')()

'''
операторы global и nonlocal используются в области видимости той функции, где требуется изменение переменной;
оператор global можно использовать как в простых функциях, так и во вложенных;
оператор nonlocal используются только во вложенных функциях;
с помощью оператора global можно определить глобальную переменную из области видимости функции, которая ранее отсутствовала;
при использовании оператора nonlocal, переменные родительской функции должны существовать.
'''


def counter(start=0):
    def update_counter():
        nonlocal start
        start += 1
        return start

    return update_counter


counter1 = counter(15)
print(counter1())
print(counter1())
print(counter1())
print(counter1())
print(counter1())

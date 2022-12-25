# https://docs.python.org/3/library/functions.html
'''
Создайте словарь, содержащий число (от 1 до n) в форме {n: n * n}. n=5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''
dict1 = {x: x * x for x in range(1, 6)}
print(dict1)

dict2 = dict()  # {}
for n in range(1, 6):
    dict2[n] = n * n
print(dict2)

'''
Получите сумму значений следующего словаря:
dict3 = {'data1': 100, 'data2': -54, 'data3': 247}  # 293
'''
dict3 = {'data1': 100, 'data2': -54, 'data3': 247}
res = 0
for i in dict3.values():
    res += i

res = sum(dict3.values())
print(res)

'''
Дан словарь dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
И дан список list1 = ['x', 'y', 'b', 'd', 'e']
Удалите из словаря те элементы, ключи которых есть в списке. На выходе должен получиться следующий словарь:
dict4 = {'a': 1, 'c': 3}
'''
dict4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
list1 = ['x', 'y', 'b', 'd', 'e']
for i, el in enumerate(list1):
    if el in dict4:
        del dict4[el]
print(dict4)

'''
Имеется словарь:
dict5 = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
Попробуйте отсортировать словарь по ключам, получив следующий словарь:
dict5 = {
    'black': '#000000',
    'green': '#008000',
    'red': '#FF0000',
    'white': '#FFFFFF'
}
'''
dict5 = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
print(dict5)
print(dict(sorted(dict5.items())))
dict5 = dict(sorted(dict5.items()))
dict5 = {k: v for k, v in sorted(dict5.items())}
print(dict5)

'''
Дан словарь:
dict6 = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
Найдите максимальное и минимальное значения словаря
'''
dict6 = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
print(min(dict6.values()))  # 20
print(max(dict6.values()))  # 5874

min_num = max_num = i = 0
for el in dict6.values():
    if i == 0:
        min_num = max_num = el
        i += 1
        continue
    if min_num > el:
        min_num = el
    if max_num < el:
        max_num = el
print(min_num, max_num)

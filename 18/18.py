# Списки (массивы) — это один из 4 встроенных типов данных в Python, используемых для хранения коллекций данных, остальные 3 — это кортежи, множестви и словари
# Списки в Python - упорядоченные изменяемые коллекции объектов произвольных типов
# список может содержать любое количество объектов любого типа (в том числе и вложенные списки), или быть пустым

empty_list = []
print(type(empty_list))
print(empty_list)

list1 = [1, 2.4, None, [1, 2, 3, True, False], 'hello']
print(list1)

# список можно создать с помощью функции list, в которую можно передать любой итерируемый объект
list2 = list('hello, world!')
print(list2)

list3 = list(range(1, 11))
print(list3)

# И еще один способ создать список - использовать генератор списков. Генератор списков - позволяет применить выражение к каждому элементу последовательности. Генераторы списков очень похожи на цикл for.
list4 = [i for i in 'Hello, world!']
print(list4)

list5 = [i for i in 'Hello, world!' if i != ',' and i != ' ' and i != '!']
print(list5)

list6 = [i for i in 'Hello, world!' if i not in [',', ' ', '!']]
print(list6)

list7 = [i.lower() for i in 'Hello, world!' if i not in [',', ' ', '!']]
print(list7)

# Распаковка коллекций

colors = ['красный', 'черный', 'белый', 'зеленый']
red = colors[0]
black = colors[1]
white = colors[2]

red, black, white, green = colors
print(red, black, white, green)

# Упаковка кортежа
colors_tuple = ('красный', 'черный', 'белый', 'зеленый')
# Распаковка кортежа
red, black, white, green = colors_tuple
print(red, black, white, green)
red, black, *other_colors = colors_tuple
print(red, black, other_colors)


# Если вы используете меньшее количество переменных в левой части, вы получите ошибку.

# Для распаковки только части элементов необходимо упаковать оставшиеся элементы в переменную с помощью *

red, black, *other_colors = colors
print(red, black, other_colors)
print(*colors)

# распаковка последовательности без переменной может быть использована для функции range
t1 = 1, 10
# print(type(t1), t1)
# print(*t1)
# for i in range(*t1):
#     print(i, end=' ')
# print([*range(*t1)])
# print(list(range(1, 10)))

# Также можно распаковать только крайние элементы
red, *other_colors, green = colors
print(red, green, other_colors)

# Или только последний
*other_colors, green = colors
print(green, other_colors)

# Распаковка может быть даже вложенной:
(*red,), black, *other_colors = colors
print(red, black, other_colors)

*l, = 'hello'
print(l)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
l3 = [*l1, *l2]
print(l3)

# Распаковка словаря в другой словарь с помощью **
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {**d1}
d2 = d1.copy()
d2 = d1
print(d1 is d2)
print(id(d1))
print(id(d2))

# Распаковка словаря
colors_d = {'red': 'красный', 'black': 'черный', 'white': 'белый', 'green': 'зеленый'}
# a, *b = colors_d  # colors_d.keys()
# a, *b = colors_d.values()  # получим значения
a, *b = colors_d.items()  # получим кортежи пар ключ:значение
print(a, b)

# Распаковка множеств
s = {'красный', 'черный', 'белый', 'зеленый'}
a, *b = s
print(a, b)

# С помощью *, можно не только распаковывать, но и объединять итерируемые объекты:
s = {'one', 'two', 'three'}
t = (4, 10)
l = [True, False, 5.4]
res = [*s, *range(*t), *t, *l]
print(res)


'''
https://www.w3schools.com/python/python_tuples_methods.asp
Если вам нужен список элементов, которые нельзя изменить, тогда вам нужен кортеж.
Кортеж — это упорядоченная и неизменяемая коллекция, неизменяемый список. Допускаются дубли значений.
'''

tuple1 = ()
print(tuple1, type(tuple1))

tuple2 = tuple()
print(tuple2, type(tuple2))

tuple1 = ('black', 'white', 'red', 'green')
print(tuple1, type(tuple1))

tuple2 = tuple(('black', 'white', 'red', 'green'))
print(tuple2, type(tuple2))

print(tuple1, id(tuple1))
# tuple1[0] = 'test'  # 'tuple' object does not support item assignment
print(len(tuple1))
print(tuple1[-1])
print(tuple1[len(tuple1) - 1])
print(tuple1[1:3])

if 'white' in tuple1:
    print('OK')

'''
После создания кортежа вы не можете изменить его значения. Кортежи неизменяемы.
Но есть обходной путь. Вы можете преобразовать кортеж в список, изменить список и снова преобразовать список в кортеж.
'''
print(tuple1)
list1 = list(tuple1)
list1[-1] = 'blue'
list1.append('orange')
tuple1 = tuple(list1)
print(tuple1)

'''
Также можно добавить элементы в кортеж, в виде второго кортежа
'''
tuple1 += tuple2
print(tuple1)

'''
Удалить элементы из кортежа можно по аналогии, преобразовав в список, а затем в кортеж. Также можно удалить весь кортеж с помощью del
'''

# Loop
for i in tuple1:
    print(i, end=' ')

print('')

for i in range(len(tuple1)):
    print(tuple1[i], end=' ')

print('')
print(tuple2)
tuple2 *= 2
print(tuple2)

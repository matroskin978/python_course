'''
Даны словари:
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
Создайте единый словарь из них, используя различные способы
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

# dict1.update({**dict2, **dict3})  # 1

# 2
# dict1 |= dict2
# dict1 |= dict3

# 3
# Python 3.8
# оператор моржа совмещает функцию присвоения значения переменной с возвратом этого значения
# print(num := 1 + 2)
# print(num)

# age = int(input('How old are you? '))
# while age < 18 or age > 65:
#     print('Wrong age')
#     age = int(input('How old are you? '))
# else:
#     print('OK')

# while (age := int(input('How old are you? '))) < 18 or age > 65:
#     print('Wrong age')
# else:
#     print('OK')

# d = {**dict2, **dict3}
# for key in (d := {**dict2, **dict3}):
#     dict1[key] = d[key]

# for d in (dict2,):
#     print(d)
#     dict1.update(d)
# print(dict1)

products = {
    'Sony': 110,
    'Samsung': 100,
    'LG': 95,
    'iPhone': 105,
}

# new_products = {}
# for title, price in products.items():
#     if price > 100:
#         new_products[title] = price

new_products = {title: price for title, price in products.items() if price > 100}
# new_products = {title: '%.2f' % (price * 1.1) for title, price in products.items() if price > 100}
# new_products = {title: price * 1.1 for title, price in products.items() if price > 100}
print(new_products)

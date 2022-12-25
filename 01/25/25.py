# ID объекта не изменяется
# months = {
#     'jan': 'January'
# }
# print(f'{months=}, {id(months)=}')
# months['feb'] = 'February'
# print(f'{months=}, {id(months)=}')

# Итерация по списку словарей
# products = [
#     {'title': 'Samsung', 'price': 1000},
#     {'title': 'Sony', 'price': 1010},
# ]
# print(products)
#
# for product in products:
#     print(f'Title: {product["title"]}, Price: {product["price"]}')

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'job': 'programmer',
    'languages': ['Python', 'C#', 'PHP', 'JS']
}
# print(person)

# Add items
# person['city'] = 'Minsk'
person.update({'city': 'Minsk'})
# person.update([('city', 'Minsk')])
# person.update({'age': 31})
# print(person)

# Remove
# del person['city']  # del by key
# if 'last_name2' in person:
#     print(person.pop('last_name2'))
# print(person.pop('last_name2', "Key doesn't exist"))
# print(person.popitem())
# print(person)

# Copy
# person2 = person.copy()
# person2 = dict(person)
# person2['age'] = 35
# print(f'{person=}, {id(person)=}')
# print(f'{person2=}, {id(person2)=}')

# Loop
# for key in person:  # person.keys()
#     print(f'{key=}, {person[key]=}')
#     # if type(person[key]) is list:
#     #     print('LIST')
#     if key == 'languages':
#         # print('LIST')
#         for lang in person[key]:
#             print(lang, end=' ')
#         print('')

# for item in person.values():
#     print(item)

# for key, item in person.items():
#     print(f'{key=}, {item=}')

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'b': 5, 'e': 6}
# Синтаксис **dict разворачивает словарь, и когда они объединяются, более позднее значение затирается более новым.
# print('{a} | {b} | {c}'.format(a=dict1['a'], b=dict1['b'], c=dict1['c']))
print('{a} | {b} | {c}'.format(**dict1))
# dict3 = {**dict1, **dict2}
# dict3 = {}
# dict3.update(dict1)
# dict3.update(dict2)

# Python 3.9 - Операторы объединения и обновления словаря
# dict1 = dict1 | dict2
# dict1 |= dict2
# print(dict1)




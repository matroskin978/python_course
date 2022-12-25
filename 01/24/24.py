'''
Словари в Python - коллекции произвольных объектов в формате пар ключ-значение, где каждый ключ связан со значением. Их иногда ещё называют ассоциативными массивами или хеш-таблицами.
Начиная с Python версии 3.7, словари упорядочены. В Python 3.6 и более ранних версиях словари неупорядочены.
Для определения пустого словаря используются фигурные скобки.
'''
dict1 = {}
print(dict1, type(dict1))

'''
Словари изменяемы, что означает, что мы можем изменять, добавлять или удалять элементы после того, как словарь был создан. В словарях не может быть двух элементов с одним и тем же ключом.
'''
dict1 = {
    "jan": "January",
    "feb": "February",
    'mar': "March",
    "apr": 'April',
    "may": "May",
    "jun": "June",
    "jul": "July",
    "aug": "August",
    "sep": "September",
    "oct": "October",
    "nov": "November",
    "dec": "Decembe",
    "dec": "December",
}
print(dict1, len(dict1))
print(dict1['sep'])
# print(dict1['test'])  # KeyError
print(dict1.get('test1', 'Value not exist'))
'''
Также можно использовать функцию dict() для создания словаря
'''
dict2 = dict(
    winter=["December", "January", "February"],
    spring=["March", "April", "May"],
    summer=["June", "July", "August"],
    autumn=["September", "October", "November"],
)
print(dict2)
print(dict2['summer'][2])

'''
Тип ключа имеет значение
'''
dict3 = {'1': 'test1', 2: 'test2', 3: 'test3'}
print(dict3)
print(dict3['1'], dict3[2])

'''
Внутри словая может быть другой словарь
'''
dict_months = {
    'winter': {
        'dec': 'December',
        'jan': 'January',
        'feb': 'February',
    },
    'spring': {
        'mar': 'March',
        'apr': 'April',
        'may': 'May',
    },
    'summer': {
        'jun': 'June',
        'jul': 'July',
        'aug': 'August',
    },
    'autumn': {
        'sep': 'September',
        'oct': 'October',
        'nov': 'November',
    }
}
print(dict_months)
print(dict_months['summer']['aug'])

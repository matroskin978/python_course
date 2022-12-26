'''
Напишите несколько решений для удаления дублирующих значений из списка list1 = ["a", "b", "a", "c", "c"]
'''

list1 = ["a", "b", "a", "c", "c"]
print(list1)

# #1
# list1 = list(set(list1))

# #2
# print(list({'a': 1, 'b': 2, 'c': 3}))  # ['a', 'b', 'c']
# list1 = list(dict.fromkeys(list1))

# #3
# res = []
# for i in list1:
#     if i not in res:
#         res.append(i)
# list1 = res.copy()

# #4
# res = []
# [res.append(i) for i in list1 if i not in res]
# list1 = res.copy()
print(list1)


'''
Напишите несколько решений поиска пересечения двух наборов:
set1 = {'a', 'b', 'c', 'd'}
set2 = {'e', 'a', 'f', 'd'}
result_set = {'a', 'd'}
'''
set1 = {'a', 'b', 'c', 'd'}
set2 = {'e', 'a', 'f', 'd'}

# result_set = set1 & set2
# result_set = set1.intersection(set2)

result_set = set()
for i in set1:
    if i in set2:
        result_set.add(i)
print(result_set)


'''
Очистите набор result_set из предыдущего задания. Попробуйте написать более одного решения
'''
# result_set -= result_set
# result_set = result_set.difference(result_set)
result_set.clear()
print(result_set)

'''
Создайте набор, содержащий разницу двух наборов:
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
result_set = {1, 2, 3}  # set3 - set4
result_set = {6, 7, 8}  # set4 - set3
'''
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
# result_set = set3 - set4
# result_set = set4 - set3
# result_set = set3.difference(set4)
result_set = set4.difference(set3)
print(result_set)

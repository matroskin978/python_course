# list1 = list(range(1, 6))
# print(list1, id(list1))
# list2 = list(range(6, 11))
# list1 += list2  # same object
# list1 = list1 + list2  # another object
# print(list1, id(list1))

# https://www.w3schools.com/python/python_lists_methods.asp
list1 = list(range(1, 11))

# del list1
# list1.clear()

# list1.append([1, 2, 3])
# list2 = list1
# list2 = list1.copy()
# list2 = list1[:]
# import copy
# list2 = copy.deepcopy(list1)
# list2 = [i for i in list1]
# list2 = list(list1)
# print(list1, list2)
# list1.append(11)
# print(list1, list2)
# list1[10].append(4)
# print(list1, list2)

# list2 = [1] * 3 + [2] + [3] * 5 + [0] * 2
# print(list2, list2.count(0))
# list2 += [True] * 2 + [False] * 3
# print(list2, list2.count(0))

# print(list1)
# list1 += ['test1', 'test2']
# t = 'test1', 'test2'
# list1.extend(t)
# list1[len(list1):] = ['test1', 'test2']
# print(list1)

# list2 = [1] * 3 + [2] + [3] * 5 + [0] * 2
# if 3 in list2:
#     print(list2, list2.index(3))

# print(list1)
# list1.reverse()
# list1 = list1[::-1]
# print(list1)

# list2 = [1] * 3 + [2] + [3] * 5 + [0] * 2
# list2 += [True] * 2 + [False] * 3
# print(list2)
# print(sorted(list2))
# list2.sort(reverse=True)
# print(list2[::-1])
# print(list2)

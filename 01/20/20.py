list1 = list(range(1, 11))
print(list1)

# ACCESSING ELEMENTS
print(list1[0])
print(list1[-1])
print(list1[len(list1) - 1])
print(list1[:])
print(list1[1:])
print(list1[1:3])
print(list1[::2])
# print('hello'[::-1])
print(list1[::-1])
print(list1[-2::-1])

i = 0
while i < len(list1):
    print(list1[i], end=' ')
    i += 1

print('')

for i in range(len(list1)):
    print(list1[i], end=' ')

print('')

for i in list1:
    print(i, end=' ')

print('')

# List Comprehensions
[print(i, end=' ') for i in list1]

print('')

# enumerate() FOR INDEX
for index, element in enumerate(list1):
    print(f'{index}:{element}', end=' ')

print('')

# MODIFYING LIST
print('*' * 20)
print(list1)
list1[0] = 'test'
print(list1)
list1[9] *= 5
print(list1)
# list1[:3] = [0, 1, 2]
list1[:3] = list(range(3))
print(list1)

print('*' * 20)

# ADDING ELEMENTS
list1.append('new element 1')
print(list1)
list1.insert(2, 'new element 2')
print(list1)
list1.insert(len(list1), 'new element 3')
print(list1)

print('*' * 20)

# REMOVING ELEMENTS
del list1[2]
print(list1)

last_el = list1.pop()
print(list1, last_el)

# el = list1.pop(len(list1) - 2)
el = list1.pop(-2)
print(list1, el)

list1.remove('new element 1')
print(list1)

if 'new element 1' in list1:
    list1.remove('new element 1')
print(list1, 'OK')

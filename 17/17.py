print('h' in 'Hello')  # False
print('H' in 'Hello')  # True
print('world' in 'Hello, world!')  # True
print('2' in '123')  # True
print('h' not in 'Hello')  # True

for letter in 'Hello world':
    print(letter, end=' ')

print('')

for letter in 'Hello world':
    if letter == ' ':
        continue
    print(letter, end=' ')

print('')

for letter in 'Hello world':
    if letter == ' ':
        break
    print(letter, end=' ')
else:
    print('!!!')

print('')

for i in range(0, 11, 2):
    if i == 0:
        continue
    print(i, end=' ')

print('')

for i in range(2, 11, 2):
    print(i, end=' ')

for i in range(2, 11, 2):
    pass

if True:
    pass

while False:
    pass
else:
    pass

print('')
num = 10
print(int((num + 1) * num / 2))

res = 0
for i in range(num + 1):
    res += i
print(res)

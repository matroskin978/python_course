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

print('*' * 20)
i = 1
while i <= 3:
    print(f'Outer loop #{i}')
    j = 1
    while j <= 5:
        print(f'\tInner loop #{j}')
        j += 1
    i += 1

for i in range(1, 4):
    print(f'Outer loop #{i}')
    for j in range(1, 6):
        print(f'\tInner loop #{j}')

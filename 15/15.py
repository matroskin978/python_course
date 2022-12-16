age = int(input('Сколько вам лет? '))

while True:  # age < 18 or age > 65
    if age < 18:
        print('Вы слишком молоды')
    elif 65 < age <= 100:
        print('Вам уже сюда не нужно')
    elif age > 100:
        print('Вы точно не ошиблись с возрастом?')
    else:
        print('Добро пожаловать!')
        break
    age = int(input('Сколько вам лет? '))

print('Добро пожаловать!')

i = 1
while i <= 10:
    if i == 4:
        i += 1
        continue
    if i == 8:
        break
    print(i, end=' ')
    i += 1
else:
    print('Oops')

print(' ')

# Homework
i = 0
while i <= 10:
    # i % 2 == 0
    # not i % 2
    # i % 2 != 0
    # i % 2
    if i % 2:
        print(i, end=' ')
    i += 1

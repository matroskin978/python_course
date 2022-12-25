age = int(input('Сколько вам лет? '))
# print(f'Вам {age} лет')
# print(int(age) + 10)
# print(type(age))

if age < 18:
    print('Вы слишком молоды')
    print('Приходите, когда вам исполнится 18')
elif 65 < age <= 100:  # age > 65 and age <= 100
    print('Вам уже сюда не нужно')
elif age > 100:
    print('Вы точно не ошиблись с возрастом?')
else:
    print('Добро пожаловать!')

print(f'Вам {age} лет')

# https://docs.python.org/3/library/random.html
'''
Создайте игру "Угадай число". Сгенерируйте случайное число от 1 до 100 которое и должен угадать игрок. Далее программа должна спросить у игрока задуманное число. Если пользователь не угадал число - программа сообщает, что загаданное число больше/меньше и предлагает попробовать еще раз, при этом программа ведет счета кол-ва попыток игрока. Если игрок угадал число, тогда программа сообщает кол-во попыток, за которое было угадано число. После этого программа предлагает сыграть еще раз или завершить игру. В зависимости от ответа программа либо генерирует новое число для угадывания, либо благодарит за игру.
'''
from random import randint

num = randint(1, 100)
cnt = 0

while True:
    user_num = int(input('Я загадал число от 1 до 100 - угадай его: '))
    cnt += 1
    if user_num == num:
        print(f'Ты угадал число за {cnt} попыток')
        more = input('Сыграем еще раз? (y/n)')
        if more == 'y':
            num = randint(1, 100)
            cnt = 0
        else:
            print('Спасибо за игру')
            break
    elif user_num > num:
        print('Мое число меньше')
    else:
        print('Мое число больше')

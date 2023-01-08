import sys

while True:
    q = input('Введи название города: ')
    if not q:
        # print('До новых встреч!')
        # exit('До новых встреч!')
        sys.exit('До новых встреч!')
    else:
        print(q)


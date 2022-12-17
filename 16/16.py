'''
Начиная с версии 3.10 в языке Python появилась такая функциональность как pattern matching (сопоставление шаблонов). Pattern matching представляет применение конструкции match, которая позволяет сопоставить выражение с некоторым шаблоном. И если выражение соответствует шаблону, то выполняются определенные действия.
'''

code = 404
match code:
    case 200:
        print(f'{code} - OK')
    case 300 | 301 | 302:
        print(f'{code} - Redirect')
    case 400 | 403 | 404:
        print(f'{code} - Client Error')
    case _:
        print(f'{code} - Server Error')


language_orig = (input('Type language (en, us, ru, de): '))
language = language_orig.lower()
# if language == 'en':
#     print('Hello')
# elif language == 'ru':
#     print('Привет')
# elif language == 'de':
#     print('Hallo')
# else:
#     print('Hmmm')

match language:
    case 'en' | 'us' if language_orig == 'EN':
        print('Hello 1')
    case 'en' | 'us':
        print('Hello 2')
    case 'ru':
        print('Привет')
    case 'de':
        print('Hallo')
    case _:
        print('Hmmm')

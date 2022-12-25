# строка — это последовательность символов. В Python все, что заключено в кавычки, является строкой. Можно использовать как одинарные, так и двойные кавычки.
s1 = 'Hello, World 1!'
s2 = "Hello, World 2!"
print(s1)
print(s2)

# использование одинарных либо двойных кавычек - дело вкуса плюс зависит от наличия кавычек в строке
s3 = "Hello, 'World' 3!"
print(s3)

# специальные символы в строке можно экранировать
s4 = "'Hello', \"World\" 4!"
print(s4)
s5 = "C:\\Python311\\news.\\txt"
print(s5)
s6 = r"C:\Python311\news.\txt"
print(s6)

# многострочные строки
s7 = 'Good frend for Iesvs sake forbeare,\n\
To digg the dvst encloased heare.\n\
Bleste be ye man yt spares thes stones,\n\
And cvrst be he yt moves my bones.'
print(s7)

print('========================')

s8 = ('Good frend for Iesvs sake forbeare,\n'
      'To digg the dvst encloased heare.\n'
      'Bleste be ye man yt spares thes stones,\n'
      'And cvrst be he yt moves my bones.')
print(s8)

print('========================')

s9 = '''\
Good frend for Iesvs sake forbeare,
To digg the dvst encloased heare.
Bleste be ye man yt spares thes stones,
And cvrst be he yt moves my bones.\
'''
print(s9)

print('========================')

s10 = """'Hello', \"World\" 5!"""
print(s10)

# конкатенация
# s11 = 'Hello, ' 'World'
s11_1 = 'Hello, '
s11_2 = 'World!'
s11 = s11_1 + s11_2
print(s11)

print('========================')

product = 'Sony'
price = 100
print("Product: " + product + "\nPrice: " + str(price))
# print(type(str(100)))
# print(type(int('100')))

print('=' * 24)

# f-strigs from Python 3.6

print(f"Product: {product}\nPrice: {price}")
print('=' * 24)

# доступ к символам строки
s12 = 'Hello, World!'
print(s12[0])
print(s12[-1])
# print(s12[13])

# strings are immutable
# s12[0] = 'h'

# slicing
# [start:end:step]
# start - include, end - exclude
'''
  0   1   2   3   4   5   6   7   8   9   10  11  12
+---+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o | , |   | W | o | r | l | d | ! | 
+---+---+---+---+---+---+---+---+---+---+---+---+---+
-13  -12 -11  10 -9  -8  -7  -6  -5  -4  -3  -2  -1 
'''
s13 = 'Hello, World!'
print(s13[0:12])
print(s13[:12])
print(s13[0:])
print(s13[:5])
print(s13[7:12])
print(s13[::2])
print(s13[::-1])
print(s13[:5] + s13[6:])
print(s13[-6:-1])
print(s13[-6:])

# len
print(len(s13))
print(s13[12])
print(s13[-1])
print(s13[len(s13) - 1])
s_len = len(s13)
print(s13[s_len - 1])

print(s13[len(s13) - len(s13)])
print(s13[-len(s13)])

'''
Homework

Дана переменная: s = 'Hello, World!'
Выведите на экран последний символ строки 4-я способами
1) используя положительный индекс
2) используя отрицательный индекс
3) используя функцию len()
4) используя функцию len() с сохранением длины строки в переменную

Выведите на экран первый символ строки 2-я способами. В обоих способах используйте функцию len()
'''

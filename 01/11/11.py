# операторы сравнения, присваивания, логические
# http://pythonicway.com/python-operators
# https://www.w3schools.com/python/python_operators.asp

# comparison
print(5 == 5)
print(5 == '5')
print(5 != '5')
# print(5 <> '5') # v2
print(5 > 5)
print(5 < 5)
print(5 >= 5)
print(5 <= 5)

# assignment
num = 10
print(num)
num = num + 5
print(num)
num += 5
print(num)
num -= 5
print(num)
num *= 5
print(num)
num /= 5
print(num)

# logical
print('and')
print(True and True)
print(True and False)
print(10 > 5 and 100 < 10)

print('or')
print(True or True)
print(True or False)
print(10 > 5 or 100 < 10)

print('not')
print(not True or True)
print(not True or False)
print(not 10 > 5 or not 100 < 10)
print(not(10 > 5 or 100 < 10))

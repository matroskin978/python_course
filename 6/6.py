# В интерактивном режиме последнее напечатанное выражение присваивается переменной _

# Python поддерживает целые числа, числа с плавающей запятой и комплексные числа.
num1 = 10
num2 = 5.4
print(type(num1))
print(type(num2))

# с числами можно производить математические операции
# http://pythonicway.com/python-operators
print(20 + 4)
print(20 - 4)
print(20 * 4)
print(20 / 4)
print(20 % 4)
print(21 % 4)
print(21 // 4)
print(20 ** 4)

# унарный оператор применяется к одному операнду
# бинарный - к обоим операндам

# Приоритет операторов
print(5 + 3 * 2)
print((5 + 3) * 2)

# print(.1 + .2)
#
# from decimal import *
# print(Decimal('.1') + Decimal('.2'))

# from Python 3.6
num3 = 1000000000
num4 = 1_000_000_000
print(num3)
print(num4)

# max number
# print(1000**1000)
num5 = 1000 ** 1000
print(type(num5))

def get_sum(a, b):
    """Sphinx Style Возращает сумму аргументов a и b.

    :param a: Первый операнд
    :param b: Второй операнд
    :type a: int | float
    :type b: int | float
    :return: Сумма параметров a + b
    :rtype: int | float
    """
    return a + b


print(get_sum(1, 2))


# https://docs.python.org/3/library/typing.html
def get_sum2(a: int | float, b: int | float) -> int | float:
    return a + b


num1: int = 2
print(get_sum2(1, 3))
list1: list[list[int]] = [[1, 2]]
print(list1)
list1 = [[2, 3], 's']
print(list1)

# https://docs.python.org/3/library/functions.html

x = 10
print(f'{x=}, {id(x)=}')
x = 11
print(f'{x=}, {id(x)=}')

print('*' * 20)

s = 'hello'
print(f'{s=}, {id(s)=}')
s += ', world'
print(f'{s=}, {id(s)=}')

print('*' * 20)

l = [1, 2, 3]
print(f'{l=}, {id(l)=}')
l.append('hello')
print(f'{l=}, {id(l)=}')

print('*' * 20)

a = b = 5
print(f'{a=}, {id(a)=}')
print(f'{b=}, {id(b)=}')
a += 2
b += 2
print(f'{a=}, {id(a)=}')
print(f'{b=}, {id(b)=}')

print('*' * 20)

l1 = [1, 2, 3, [4, 5]]
# l2 = l1
l2 = l1.copy()
# import copy
# l2 = copy.deepcopy(l1)
print(f'{l1=}, {id(l1)=}')
print(f'{l2=}, {id(l2)=}')
l1.append(4)
print(f'{l1=}, {id(l1)=}')
print(f'{l2=}, {id(l2)=}')

print('*' * 20)

l3 = [1, 2, 3]
print(f'{l3=}, {id(l3)=}')
# l3 += [4, 5]  # same object
l3 = l3 + [4, 5]  # another object
print(f'{l3=}, {id(l3)=}')

print(dir([]))
l5 = [1, 2]
print(f'{l5=}, {id(l5)=}')
l5 = l5.__iadd__([3, 4])  # same object
l5 = l5.__add__([3, 4])  # another object
print(f'{l5=}, {id(l5)=}')
# print([1, 2].__add__([3, 4]))
# print([1, 2].__iadd__([3, 4]))
# print(help([].__add__))

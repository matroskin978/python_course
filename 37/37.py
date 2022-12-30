import sys
# sys.path.append(r'C:\Users\Andrey\Desktop\python\modules')

import pprint
# import my_module
# import modules.my_module as m
# from my_module import file_name, print_name
# from my_module import file_name as fm, print_name as pn
from modules.my_module import *
# import my_package
import my_package.file1 as mp_f1, my_package.file2 as mp_f2

pprint.pp(sys.path)
# m.pprint.pp(sys.path)

mp_f1.file1_fn()
mp_f1.file1_fn2()
mp_f2.file2_fn()
mp_f2.file2_fn2()

# cities = [
#     ['Mexico', 8_855_000],
#     ['Paris', 2_161_000],
#     ['Minsk', 1_975_000],
#     ['Rio de Janeiro', 6_748_000],
#     ['Tokio', 13_960_000],
# ]
# print(cities)

# print(dir(pprint))
# pprint.pp(cities)

# my_module.print_name()
# print(dir(my_package))
# print(my_package.TEST)
# print(dir())

print_name()
# m.print_name()
# pn()
# print_name()


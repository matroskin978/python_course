import pprint

__all__ = ['print_name', 'file_name', 'fn1']

file_name = 'Filename: my_module.py'


def print_name():
    print(file_name, __name__)


def fn1():
    print('FN1')


if __name__ == '__main__':
    print_name()

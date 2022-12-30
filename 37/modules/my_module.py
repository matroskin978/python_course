import pprint

file_name = 'Filename: my_module.py'


def print_name():
    print(file_name, __name__)


if __name__ == '__main__':
    print_name()

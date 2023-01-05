# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://www.geeksforgeeks.org/reading-writing-text-files-python/
import xlsxwriter

# Read
# f = open('file.txt', mode='r', encoding='utf-8')

# print(f)
# text1 = f.read(1)
# text2 = f.read(1)
# print(text1)
# print(text2)
# text = f.read()
# print(text)
#
# f.close()

# with open('file.txt', mode='r', encoding='utf-8') as f:
    # print(f.readlines())  # read lines in list
    # print(list(f))  # the same
    # print(f.readline())  # read one string
    # for line in f:
    #     print(line.rstrip('\n'))

# Write
# f = open('file.txt', mode='a', encoding='utf-8')
# f.write('Новая строка 1\n')
# f.write('Новая строка 2\n')
# f.close()

# lines = ['Новая строка 3', 'Новая строка 4']
# lines2 = ['Новая строка 5', 'Новая строка 6']
# f = open('file.txt', mode='a', encoding='utf-8')
# for line in lines:
#     f.write(f'{line}\n')
# f.writelines(lines2)
# f.writelines(f'{i}\n' for i in lines2)
# f.close()

# with open('file.txt', mode='a+', encoding='utf-8') as f:
#     f.write('Test\n')
#     f.seek(0)
#     print(list(f))

# with open('file2.txt', mode='a+', encoding='utf-8') as f:
#     f.write('Test\n')
#     f.seek(0)
#     print(list(f))

# Python 3.10
# with (
#     open('file.txt', mode='r', encoding='utf=8') as f1,
#     open('file2.txt', mode='r', encoding='utf=8') as f2
# ):
#     print(list(f1))
#     print('*' * 20)
#     print(list(f2))

# with open('file.txt', mode='r', encoding='utf-8') as f:
#     f.seek(1 * 2)
#     print(f.read(2))

with open('file.txt', mode='r', encoding='utf-8') as f:
    print(lines := f.readlines())
    workbook = xlsxwriter.Workbook('demo.xlsx')
    worksheet = workbook.add_worksheet()
    row = column = 0
    for line in lines:
        worksheet.write(row, column, line)
        row += 1
    workbook.close()

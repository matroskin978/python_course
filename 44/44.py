# https://docs.python.org/3/tutorial/errors.html
i = 0

while True:
    try:
        num = int(input('Enter a number > 0: '))
        res = 10 / num
        if num == 1:
            raise ZeroDivisionError
        if num == 10:
            raise NameError('TEST ERROR!')
        # break
    except ValueError:
        print("Ooops! This is not a number.")
    except ZeroDivisionError:
        print("Ooops! The number must be > 0")
    # except:
    #     print("Something error")
    else:
        print(res)
        break
    finally:
        i += 1
        print(f'Count: {i}')

# print(res)

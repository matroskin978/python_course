'''
https://docs.python.org/3/library/datetime.html
https://otus.ru/journal/modul-datetime-v-python/
Модуль datetime предоставляет классы для работы с датой и временем.
Модуль предлагает следующие классы:

Класс datetime.date(year, month, day) - стандартная дата. Атрибуты: year, month, day. Неизменяемый объект.

Класс datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - стандартное время, не зависит от даты. Атрибуты: hour, minute, second, microsecond, tzinfo.

Класс datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None) - комбинация даты и времени.

Класс datetime.timedelta - разница между двумя моментами времени, с точностью до микросекунд.

Класс datetime.tzinfo - абстрактный базовый класс для информации о временной зоне (например, для учета часового пояса и / или летнего времени).

Класс datetime.timezone - класс, который реализует абстрактный базовый класс tzinfo.
'''

# импортируем весь модуль
import datetime

# print(locals())
print(datetime.datetime.now())  # 2023-01-01 09:23:36.325312
print(datetime.date.today())  # 2023-01-01

# можно импортировать только нужный класс
# from datetime import datetime
#
# print(datetime.now())


# Класс date позволяет работать с датой и создавать объект даты
print(datetime.date(2000, 12, 20))  # 2000-12-20
# или через datetime
print(datetime.datetime(2000, 12, 20))  # 2000-12-20 00:00:00
print(datetime.datetime(2000, 12, 20, 10, 20, 30))  # 2000-12-20 10:20:30

# Также существует возможность создавать объекты date, используя метку времени — timestamp. Для преобразования метки времени в дату в Python используют метод fromtimestamp.
print(datetime.date.fromtimestamp(1))  # 1970-01-01
print(datetime.date.fromtimestamp(60 * 60 * 22 - 1))  # 1970-01-01
print(datetime.datetime.fromtimestamp(1))  # 1970-01-01 02:00:01

# Из объекта date можно без проблем получить текущие значения дня, года, месяца:
print(datetime.date.today())  # 2023-01-01
print(datetime.date.today().year)  # 2023
print(datetime.date.today().month)  # 1
print(datetime.date.today().day)  # 1


# Класс time. Экземпляр класса time отвечает за время, куда входит широкий спектр данных (data): и часы, и минуты, и секунды, и даже микросекунды.
print(datetime.datetime.now().hour)  # hours
print(datetime.datetime.now().minute)  # minutes
print(datetime.datetime.now().second)  # seconds

# для работы с временем можно использовать модуль time
# import time
# print(t := time.localtime())
# print(time.strftime('%H:%M:%S', t))
# time.sleep(3)
# print(t := time.localtime())
# print(time.strftime('%H:%M:%S', t))

# форматирование даты возможно и для модуля datetime
print(datetime.date.today().strftime('%b %B %a %A %d'))
print(datetime.date.today().strftime('%d %B %Y'))
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.datetime.today().strftime('%d.%m.%Y %H:%M:%S'))

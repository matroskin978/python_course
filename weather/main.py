# https://openweathermap.org/current
# https://pypi.org/project/requests/
from funcs import get_weather, print_weather, save_excel

print("*" * 70)
print("""* Привет! Я помогу узнать погоду в любом городе мира.
* Просто введи запрос в формате city[,country_code]
* Если нужно выйти из программы, тогда просто нажми Enter""")
print("*" * 70)

while True:
    q = input('Введи название города: ')
    if not q:
        print('До новых встреч!')
        break
    else:
        weather = get_weather(q)
        print_weather(weather)
        save_excel(weather)

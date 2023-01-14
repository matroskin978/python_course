# https://pypi.org/project/pyinstaller/
# pyinstaller --noconfirm --onedir --windowed --add-data "<CustomTkinter Location>/customtkinter;customtkinter/"  "<Path to Python Script>"
# pyinstaller --noconfirm --onedir --windowed -i "C:\Users\Andrey\Desktop\python\weather_gui\weather_app.ico" --distpath "C:\Users\Andrey\Desktop\python\weather_gui\program" --add-data "c:\users\andrey\desktop\python\venv\lib\site-packages\customtkinter;customtkinter\" --add-data "C:\Users\Andrey\Desktop\python\weather_gui\weather_icon.png;." main.py
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import datetime
import locale
from PIL import Image
import requests

API_KEY = '5e1ce895b1f7950c8267adecc8ce4989'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'
UNITS = 'metric'
LANG = 'ru'

root = ctk.CTk()
root.iconphoto(False, tk.PhotoImage(file="weather_icon.png"))
root.title("Weather App")
root.geometry("800x500+400+100")
root.resizable(False, False)
root.configure(fg_color="#fb8c00")


def get_date_time(ts, timezone, dt_format="%H:%M:%S"):
    tz = datetime.timezone(datetime.timedelta(seconds=timezone))
    return datetime.datetime.fromtimestamp(ts, tz=tz).strftime(dt_format)


def get_weather(event=""):
    params = {
        "appid": API_KEY,
        "units": UNITS,
        "lang": LANG,
        "q": search_entry.get()
    }
    try:
        r = requests.get(API_URL, params=params)
        weather = r.json()
        print_weather(weather)
    except:
        print_weather({"cod": 0, "message": "Не удалось получить данные"})


def print_weather(data):
    search_entry.delete(0, "end")
    if data['cod'] != 200:
        messagebox.showerror("Ошибка", data['message'].ljust(50))
        content_frame.pack_forget()
        start_content_frame.pack(fill="both", expand=True, side="top", anchor='nw')
        # welcome_label.configure(text=data["message"])
        city_label.configure(text="")
    else:
        start_content_frame.pack_forget()
        content_frame.pack(fill="both", expand=True, side="top", anchor='nw')

        city = f"{data['name']}, {data['sys']['country']}"
        city_label.configure(text=city)
        city_cnt_label.configure(text=city)
        temp_label.configure(text=f"{data['main']['temp']} °C")
        sunrise_time = get_date_time(data['sys']['sunrise'], data['timezone'])
        sunset_time = get_date_time(data['sys']['sunset'], data['timezone'])
        data_text = f"""Местоположение: {data['name']}, {data['sys']['country']}
Температура: {data['main']['temp']} °C
Атм. давление: {data['main']['pressure']} гПа
Влажность: {data['main']['humidity']}%
Скорость ветра: {data['wind']['speed']} м/с
Погодные условия: {data['weather'][0]['description']}
Восход: {sunrise_time}
Закат: {sunset_time}"""
        data_textbox.place(x=450, y=150)
        data_textbox.configure(state="normal")
        data_textbox.delete("0.0", "end")
        data_textbox.insert('1.0', data_text)
        data_textbox.configure(state="disabled")


# Top Frame
top_frame = ctk.CTkFrame(root, width=800, height=50, fg_color="#212121", corner_radius=0)
top_frame.pack(fill='x')
# top_frame.pack()

# City Label
# font=("Roboto", 15)
city_font = ctk.CTkFont(size=15)
city_label = ctk.CTkLabel(top_frame, text='Название города', text_color='#fff', font=city_font)
city_label.place(x=20, y=10)

# Search
search_entry = ctk.CTkEntry(top_frame, placeholder_text="Type city...")
search_entry.place(x=520, y=10)

# https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
# https://www.pythontutorial.net/tkinter/tkinter-event-binding/
search_entry.bind("<Return>", get_weather)

search_btn = ctk.CTkButton(top_frame, text="Search", width=100, command=get_weather)
search_btn.place(x=670, y=10)

# Start Content Frame
start_content_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#fb8c00")
start_content_frame.pack(fill="both", expand=True, side="top", anchor='nw')

welcome_font = ctk.CTkFont(size=30)
welcome_label = ctk.CTkLabel(start_content_frame, text="Добро пожаловать в программу показа погоды", text_color="#fff", font=welcome_font)
welcome_label.place(relx=0.5, rely=0.5, anchor='center')

# Content Frame
content_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="#fb8c00")
# content_frame.pack(fill="both", expand=True, side="top", anchor='nw')

# Date
locale.setlocale(locale.LC_TIME, "ru")
curr_date = datetime.datetime.now().strftime("%a, %B %d")
date_font = ctk.CTkFont(size=20)
date_label = ctk.CTkLabel(content_frame, text=curr_date, text_color="#fff", font=date_font)
date_label.place(relx=0.5, y=30, anchor='center')

# City
city_cnt_font = ctk.CTkFont(size=20)
city_cnt_label = ctk.CTkLabel(content_frame, text="Название города", text_color="#fff", font=city_cnt_font)
city_cnt_label.place(relx=0.5, y=60, anchor='center')

# Icon
weather_icon = ctk.CTkImage(light_image=Image.open("./weather_icon.png"), size=(150, 150))
weather_icon_label = ctk.CTkLabel(content_frame, text="", image=weather_icon)
weather_icon_label.place(x=30, y=120)

# Temperature
temp_font = ctk.CTkFont(size=50)
temp_label = ctk.CTkLabel(content_frame, text="25 °C", text_color="#fff", font=temp_font)
temp_label.place(x=200, y=150)

# Other data
data_textbox_font = ctk.CTkFont(size=15, weight="bold")
data_textbox = ctk.CTkTextbox(content_frame, fg_color="#e65100", text_color="#fff", width=300, height=250, font=data_textbox_font, spacing3=5, wrap="word", activate_scrollbars=False)
# data_textbox.place(x=400, y=150)
# data_text = """Местоположение: Название города
# Температура: 25 °C
# Атм. давление: 1000 гПа
# Влажность: 70%
# Скорость ветра: 15 м/с
# Погодные условия: Солнечно
# Восход: 08:00
# Закат: 17:00"""
# data_textbox.insert("0.0", data_text)
# data_textbox.configure(state="disabled")

root.mainloop()

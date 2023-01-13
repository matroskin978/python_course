# https://tkdocs.com/tutorial/styles.html
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme='')
root.title('ttkthemes')
root.geometry('500x400+400+100')

style = ttk.Style()
# print(style.theme_names(), style.theme_use())
# style.theme_use('radiance')


def choose_theme(event):
    style.theme_use(themes_box.get())


ttk.Button(root, text='Button').pack(pady=10)
ttk.Entry(root).pack()
ttk.Label(root, text='Hello world!').pack(pady=10)

themes = [style.theme_use(), 'adapta', 'arc', 'black', 'equilux', 'plastik', 'radiance', 'yaru']
themes_box = ttk.Combobox(root, values=themes)
themes_box.current(0)
themes_box.pack(pady=10)
themes_box.bind('<<ComboboxSelected>>', choose_theme)

root.mainloop()

import tkinter as tk
import random

COLORS = [('#e53935', '#fff'), ('#4a148c', '#fff'), ('#bbdefb', 'black'), ('#ff9800', 'black')]

root = tk.Tk()
root.title('Label Widget')
root.geometry('500x400')


def get_label():
    # print(label.cget('text'))
    print(label_text.get())


def set_label():
    # label['text'] = 'TEST'
    label_text.set('Hello, World!')


def change_label_color():
    idx = random.randint(0, len(COLORS) - 1)
    color = COLORS[idx]
    label['bg'] = color[0]
    label['fg'] = color[1]


label_text = tk.StringVar()
label_text.set('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris quis placerat tortor. Maecenas nisi metus, bibendum in placerat id, accumsan in eros!')

btn = tk.Button(root, text='Get', font="Verdana 12", width=12, padx=5, pady=5, command=get_label)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Set', font="Verdana 12", width=12, padx=5, pady=5, command=set_label)
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Change color', font="Verdana 12", width=12, padx=5, pady=5, command=change_label_color)
btn3.pack(pady=10)

label = tk.Label(root, textvariable=label_text, bg='black', fg='white', width=40, height=10, padx=5, font="Verdana 12", cursor='watch', anchor='nw', wraplength=400, justify='left')
label.pack(pady=10)

root.mainloop()

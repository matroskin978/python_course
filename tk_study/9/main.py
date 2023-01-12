# https://tkdocs.com/tutorial/styles.html
import tkinter as tk
from tkinter import ttk
from calendar import month_name

root = tk.Tk()
root.title('ttk')
root.geometry('500x400+400+100')

style = ttk.Style()
print(style.theme_names(), style.theme_use())
# style.theme_use('clam')

# print(ttk.Button().winfo_class())  # TButton
# style.configure('.', foreground='#cc0000')
style.configure('TButton', padding='30 10 30 10')
style.configure('My.TButton', foreground='#ff0000')

tk.Button(root, text='TK Button').pack(pady=10)
ttk.Button(root, text='TTK Button', width=20).pack()
ttk.Button(root, text='TTK Button', width=20, style='My.TButton').pack(pady=10)

tk.Entry(root).pack(pady=10)
ttk.Entry(root).pack()


def choose_month(event):
    print(months_box.current(), months_box.get())


# https://www.pythontutorial.net/tkinter/tkinter-ttk/
months = list(month_name)[1:]
months_box = ttk.Combobox(root, values=months)
# months = list(month_name)[1:]
# print(months)
# months_box['values'] = list(month_name)[1:]
months_box.current(0)
months_box.pack(pady=10)
months_box.bind('<<ComboboxSelected>>', choose_month)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, expand=True, fill='both')

frame1 = ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill='both', expand=True)

frame2 = ttk.Frame(notebook, width=400, height=280)
frame2.pack(fill='both', expand=True)

ttk.Button(frame1, text='General Button').pack()
ttk.Button(frame2, text='Profile Button').pack()

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')

root.mainloop()

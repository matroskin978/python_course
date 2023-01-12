import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.title('Place')
root.geometry('500x400+400+100')


def add_content():
    textarea.insert('2.4', 'HELLO')
    textarea.insert('end', 'HELLO')


def clear_content():
    textarea.delete('1.0', 'end')


def get_content():
    print(textarea.get('1.0', 'end'))


menu_frame = tk.Frame(root, bg='#37474f')
menu_frame.pack(fill='x')

content_frame = tk.Frame(root, bg='#78909c')
content_frame.pack(fill='both', expand=True)

tk.Button(menu_frame, text="Add", pady=5, command=add_content).grid(row=0, column=0, sticky='we', pady=5, padx=5)
tk.Button(menu_frame, text="Clear", pady=5, command=clear_content).grid(row=0, column=1, sticky='we', pady=5, padx=5)
tk.Button(menu_frame, text="Get", pady=5, command=get_content).grid(row=0, column=2, sticky='we', pady=5, padx=5)
menu_frame.grid_columnconfigure('all', weight=1)
'''
Вес определяет ширину столбца относительно других столбцов.
Например, столбец с весом 2 будет в два раза шире столбца с весом 1.
'''

# textarea = tk.Text(content_frame, bg="#263238", fg="#fff", padx=10, pady=10, wrap='word', insertbackground="#eda756", selectbackground="#4e5a65", spacing3=15, spacing2=5)
# textarea.pack(fill='both', expand=True, padx=5, pady=5)

textarea = ScrolledText(content_frame, bg="#263238", fg="#fff", padx=10, pady=10, wrap='word', insertbackground="#eda756", selectbackground="#4e5a65", spacing3=15, spacing2=5)
textarea.pack(fill='both', expand=True, padx=5, pady=5)

# 'line.column'
# textarea.insert('1.0', 'Hello, world!')

root.mainloop()

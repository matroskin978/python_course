import tkinter as tk

root = tk.Tk()
root.title('Grid')
# root.geometry('500x400+400+100')

# f = tk.Frame(root, pady=10)
# f.pack()
#
# tk.Button(f, text='7', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=0, column=0, pady=2, padx=2)
# tk.Button(f, text='8', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=0, column=1, pady=2, padx=2)
# tk.Button(f, text='9', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=0, column=2, pady=2, padx=2)
# tk.Button(f, text='4', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=1, column=0, pady=2, padx=2)
# tk.Button(f, text='5', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=1, column=1, pady=2, padx=2)
# tk.Button(f, text='6', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=1, column=2, pady=2, padx=2)
# tk.Button(f, text='1', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=2, column=0, pady=2, padx=2)
# tk.Button(f, text='2', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=2, column=1, pady=2, padx=2)
# tk.Button(f, text='3', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=2, column=2, pady=2, padx=2)
# tk.Button(f, text='0', padx=15, pady=10, bg='#fafafa', font='Verdana 12', borderwidth=1).grid(row=3, column=1, pady=2, padx=2)

tk.Label(root, text="Login:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root).grid(row=0, column=1, columnspan=2, padx=10, sticky='we')

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, sticky='w')
tk.Entry(root, show='*').grid(row=1, column=1, columnspan=2, padx=10, sticky='we')

tk.Button(root, text="Login", padx=5).grid(row=2, column=0, padx=10, pady=10, sticky='w')
tk.Button(root, text="Register", padx=5).grid(row=2, column=1)
tk.Button(root, text="Forgot password?", padx=5).grid(row=2, column=2, padx=10)

root.mainloop()

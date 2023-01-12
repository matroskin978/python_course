import tkinter as tk

root = tk.Tk()
root.title('Place')
root.geometry('500x400+400+100')

tk.Label(root, text='Hello, world!', padx=20, pady=10, bg='#37474f', fg='#fff', font=12).place(x=0, y=0, anchor='nw')

# tk.Entry(root).place(x=10, y=10, width=250, height=40)
# tk.Button(root, text='Send').place(x=270, y=10, height=40, width=100)
#
# tk.Entry(root).place(x=10, y=70, width=250, height=40)
# tk.Button(root, text='Send2').place(x=270, y=70, height=40, width=100)

COLORS = [('#e53935', '#fff'), ('#4a148c', '#fff'), ('#bbdefb', 'black'), ('#ff9800', 'black')]

# tk.Label(root, text='1', font=12, width=8, height=4, bg='#e53935', fg='#fff').place(x=0, y=0)
# tk.Label(root, text='2', font=12, width=8, height=4, bg='#4a148c', fg='#fff').place(x=500, y=0, anchor='ne')
# tk.Label(root, text='3', font=12, width=8, height=4, bg='#bbdefb', fg='#000').place(x=0, y=400, anchor='sw')
# tk.Label(root, text='4', font=12, width=8, height=4, bg='#ff9800', fg='#000').place(x=500, y=400, anchor='se')
# tk.Label(root, text='5', font=12, width=8, height=4, bg='#b0bec5', fg='#000').place(x=250, y=200, anchor='center')
# tk.Label(root, text='6', font=12, width=8, height=4, bg='#b0bec5', fg='#000').place(relx=0.5, rely=0.5, anchor='center')

# f1 = tk.Frame(root, bg='#000')
# f1.place(relwidth=0.9, relheight=0.1, relx=0.5, rely=0.05, anchor='n')
# f1.place(relwidth=0.9, relheight=0.1, relx=0.05, rely=0.05)

# tk.Entry(f1).place(relwidth=0.7, relheight=0.9, rely=0.05, relx=0.01, anchor='nw')
# tk.Button(f1, text='Send').place(relwidth=0.27, relheight=.9, rely=0.05, relx=0.72, anchor='nw')

root.mainloop()

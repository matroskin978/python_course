import tkinter as tk

root = tk.Tk()
root.title('Pack')
root.geometry('500x400+400+100')

# default
# tk.Label(root, text='1', bg='#e53935', fg='#fff', width=8, height=4).pack()
# tk.Label(root, text='2', bg='#8e24aa', fg='#fff', width=8, height=4).pack()
# tk.Label(root, text='3', bg='#1e88e5', fg='#fff', width=8, height=4).pack()
# tk.Label(root, text='4', bg='#00897b', fg='#fff', width=8, height=4).pack()

# left-center
# tk.Label(root, text='1', bg='#e53935', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='left')
# tk.Label(root, text='2', bg='#8e24aa', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='left')
# tk.Label(root, text='3', bg='#1e88e5', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='left')
# tk.Label(root, text='4', bg='#00897b', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='left')

# left-top
# tk.Label(root, text='1', bg='#e53935', fg='#fff', width=6, height=3, font='Verdana, 12').pack(anchor='nw')
# tk.Label(root, text='2', bg='#8e24aa', fg='#fff', width=6, height=3, font='Verdana, 12').pack(anchor='nw')
# tk.Label(root, text='3', bg='#1e88e5', fg='#fff', width=6, height=3, font='Verdana, 12').pack(anchor='nw')
# tk.Label(root, text='4', bg='#00897b', fg='#fff', width=6, height=3, font='Verdana, 12').pack(anchor='nw')

frame1 = tk.Frame(root, bg='#000')
frame1.pack(fill='x')
frame2 = tk.Frame(root, bg='#fff')
frame2.pack(fill='both', side='bottom')

# tk.Label(frame1, text='1', bg='#e53935', fg='#fff', width=6, height=3, font='Verdana, 12').pack(anchor='nw')
# tk.Label(frame2, text='2', bg='#8e24aa', fg='#fff', width=6, height=3, font='Verdana, 12').grid()


tk.Label(frame1, text='1', bg='#e53935', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='left', anchor='n')
tk.Label(frame1, text='2', bg='#8e24aa', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='right', anchor='n')
tk.Label(frame2, text='3', bg='#1e88e5', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='left', anchor='n')
tk.Label(frame2, text='4', bg='#00897b', fg='#fff', width=6, height=3, font='Verdana, 12').pack(side='right', anchor='n')

root.mainloop()

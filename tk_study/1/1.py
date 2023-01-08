# https://docs.python.org/3/library/tk.html
# https://www.tutorialspoint.com/python3/python_gui_programming.htm
import tkinter as tk

root = tk.Tk()
root.title('Тестовое приложение')
# root.maxsize(300, 300)
# root.geometry('500x500+500+100')
# root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
# center window
w = 500
h = 300
s_w = root.winfo_screenwidth()
s_h = root.winfo_screenheight()
x = int((s_w / 2) - (w / 2))
y = int((s_h / 2) - (h / 2))
root.geometry(f'{w}x{h}+{x}+{y}')
# root.geometry('700x400')
# root.resizable(False, False)
root.iconbitmap('logo.ico')
# img = tk.PhotoImage(file='logo.png')
# root.iconphoto(False, tk.PhotoImage(file='logo.png'))
# root.config(bg='#000')
# root.configure(bg='red')
root['bg'] = 'black'

root.mainloop()

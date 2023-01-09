import tkinter as tk
import time

root = tk.Tk()
root.title('Button Widget')
w = 500
h = 300
s_w = root.winfo_screenwidth()
s_h = root.winfo_screenheight()
x = int((s_w / 2) - (w / 2))
y = int((s_h / 2) - (h / 2))
root.geometry(f'{w}x{h}+{x}+{y}')


def my_fn():
    print('Clicked')
    if btn['width'] == 12:
        btn['width'] = 20
    else:
        btn['width'] = 12
    btn['text'] = 'Clicked' if btn['text'] == 'Press me' else 'Press me'


def my_fn2(text):
    print(text)


def update_time():
    btn4['text'] = 'Time: ' + time.strftime('%H:%M:%S')


time_now = time.strftime('%H:%M:%S')

btn = tk.Button(root, text='Press me', font="Verdana 12", width=12, padx=5, pady=5, command=my_fn)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Button 2', font="Verdana 12", width=12, padx=5, pady=5, command=lambda: my_fn2('Button 2'))
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Button 3', font=("Times New Roman", 15), width=12, padx=5, pady=5, command=lambda: print('Hello'))
btn3.pack(pady=10)

btn4 = tk.Button(root, text=f'Time: {time_now}', font="Verdana 12", width=12, padx=5, pady=5, command=update_time)
btn4.pack(pady=10)

root.mainloop()

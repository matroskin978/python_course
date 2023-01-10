import tkinter as tk

root = tk.Tk()
root.title('Entry Widget')
root.geometry('500x400+400+100')


def get_inp1():
    print(text := inp1.get())
    print(inp1_text.get())
    label['text'] = text


def set_inp1():
    clear_inp1()
    # inp1_text.set('New text')
    inp1.insert(0, 'New text')


def clear_inp1():
    inp1.delete(0, 'end')


inp1_text = tk.StringVar()
inp1_text.set('Test')

inp1 = tk.Entry(root, justify='left', textvariable=inp1_text)
# inp1.insert(0, '111')
# inp1.insert('end', '222')  # tk.END
inp1.pack(pady=10)

btn = tk.Button(root, text='Get', font="Verdana 12", width=12, padx=5, pady=5, command=get_inp1)
btn.pack(pady=10)

btn2 = tk.Button(root, text='Set', font="Verdana 12", width=12, padx=5, pady=5, command=set_inp1)
btn2.pack(pady=10)

btn3 = tk.Button(root, text='Clear', font="Verdana 12", width=12, padx=5, pady=5, command=clear_inp1)
btn3.pack(pady=10)

label = tk.Label(root, bg='black', fg='white', width=40, padx=5, font="Verdana 12", cursor='watch', anchor='nw', wraplength=400, justify='left')
label.pack(pady=10)

root.mainloop()

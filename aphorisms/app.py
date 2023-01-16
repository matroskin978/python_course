# https://stihionline.ru/rubai-omara-hajyama/
# import tkinter as tk
import customtkinter as ctk
import sqlite3
from tkinter import messagebox


def get_data():
    with sqlite3.connect('app.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS poems (id INTEGER PRIMARY KEY, poem TEXT NOT NULL)")
        try:
            cursor.execute("SELECT * FROM poems ORDER BY RANDOM() LIMIT 1")
        except:
            return {"id": 0, "poem": "Ошибка!"}
        return cursor.fetchone()


def update_poem():
    row_id = 0 if not label_id.cget("text") else label_id.cget("text")
    with sqlite3.connect('app.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) AS cnt FROM poems")
        if cursor.fetchone()["cnt"] > 1:
            cursor.execute("SELECT * FROM poems WHERE id != ? ORDER BY RANDOM() LIMIT 1", (row_id,))
        else:
            cursor.execute("SELECT * FROM poems LIMIT 1")
        data_poem = cursor.fetchone()
        if data_poem:
            label_id.configure(text=data_poem["id"])
            textbox_1.delete("0.0", "end")
            textbox_1.insert("insert", data_poem["poem"])
        else:
            textbox_1.delete("0.0", "end")
            textbox_1.insert("insert", "Данных в БД нет...")


def insert_poem():
    new_poem = textbox_2.get("0.0", "end").strip()
    if new_poem:
        with sqlite3.connect('app.db') as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO poems (poem) VALUES (?)", (new_poem,))
            db.commit()
            textbox_2.delete("0.0", "end")
            messagebox.showinfo("Готово!", "Стихотворение добавлено в БД.")
    else:
        messagebox.showwarning("Заполните поле", "Для добавления в БД стихотворения необходимо ввести его в соответствующее поле.")


data = get_data()

ctk.set_appearance_mode("system")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("600x500")
app.title("Рубаи Омара Хайяма")
app.resizable(False, False)

# Tab
tabview = ctk.CTkTabview(master=app)
tabview.pack(pady=20, padx=50, fill="both", expand=True)

tab_1 = tabview.add("Случайное")
tab_2 = tabview.add("Добавить")

# Tab 1
label_id = ctk.CTkLabel(master=tab_1, text="")
label_id.pack()

if data:
    label_id.configure(text=data["id"])
textbox_1 = ctk.CTkTextbox(master=tab_1, width=450, height=300, wrap="word", spacing3=10)
textbox_1.pack()

example = """Не завидуй тому, кто силен и богат,
за рассветом всегда наступает закат.
С этой жизнью короткою, равною вдоху,
Обращайся, как с данной тебе напрокат."""
if data:
    textbox_1.insert("0.0", data["poem"])  # insert at line 0 character 0 or "insert"

button_1 = ctk.CTkButton(tab_1, text="Обновить", command=update_poem)
button_1.pack(pady=20)

# Tab 2
textbox_2 = ctk.CTkTextbox(master=tab_2, width=450, height=300, wrap="word", spacing3=10)
textbox_2.pack()
button_2 = ctk.CTkButton(tab_2, text="Сохранить", command=insert_poem)
button_2.pack(pady=20)

app.mainloop()

# pyinstaller --noconfirm --onedir --windowed -i "C:\Users\Andrey\Desktop\python\aphorisms\poetry.ico" --distpath "C:\Users\Andrey\Desktop\python\aphorisms\program" --add-data "c:\users\andrey\desktop\python\venv\lib\site-packages\customtkinter;customtkinter\" app.py

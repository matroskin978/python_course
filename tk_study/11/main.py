# https://github.com/TomSchimansky/CustomTkinter
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
# ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
# ctk.set_default_color_theme("mytheme.json")

root = ctk.CTk()
root.title("Custom Tkinter")
root.geometry("500x400+400+100")
# root.configure(fg_color="#000")

tk.Button(root, text="TK Button").pack(pady=10)
# ctk.CTkButton(root, text="CTK Button", fg_color=("#DB3E39", "#821D1A")).pack()
ctk.CTkButton(root, text="CTK Button").pack()
ctk.CTkButton(root, text="CTK Button2", width=150, height=40, fg_color="#242424", border_color="#000", border_width=1, corner_radius=20, hover_color="#000", text_color="#fff").pack(pady=10)

root.mainloop()

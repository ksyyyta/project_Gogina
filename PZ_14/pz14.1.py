"""
вариант 4
"""
import tkinter as tk
from tkinter import ttk

def submit_form():
    name = entry_name.get()
    password = entry_password.get()
    age = entry_age.get()
    gender = gender_var.get()

    hobbies = []
    if hobby_music.get():
        hobbies.append("Музыка")
    if hobby_video.get():
        hobbies.append("Видео")
    if hobby_drawing.get():
        hobbies.append("Рисование")

    country = country_var.get()
    city = entry_city.get()
    about = text_about.get("1.0", tk.END).strip()
    math_result = entry_math.get()
    pass

def clear_form():
    entry_name.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    gender_var.set("")
    hobby_music.set(False)
    hobby_video.set(False)
    hobby_drawing.set(False)
    country_var.set("")
    entry_city.delete(0, tk.END)
    text_about.delete("1.0", tk.END)
    entry_math.delete(0, tk.END)

root = tk.Tk()
root.title("Форма регистрации")
root.geometry("400x600")

tk.Label(root, text="Форма регистрации пользователя",
         font=("Arial", 14, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

tk.Label(frame, text="Ваше имя:").pack(anchor="w", pady=(10,0))
entry_name = tk.Entry(frame, width=40)
entry_name.pack(fill="x", pady=(0,10))

tk.Label(frame, text="Пароль:").pack(anchor="w")
entry_password = tk.Entry(frame, show="*", width=40)
entry_password.pack(fill="x", pady=(0,10))

tk.Label(frame, text="Возраст:").pack(anchor="w")
entry_age = tk.Entry(frame, width=40)
entry_age.pack(fill="x", pady=(0,10))

tk.Label(frame, text="Пол:").pack(anchor="w")
gender_var = tk.StringVar()
gender_frame = tk.Frame(frame)
gender_frame.pack(fill="x", pady=(5,10))
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var,
               value="Мужской").pack(side="left", padx=10)
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var,
               value="Женский").pack(side="left", padx=10)

tk.Label(frame, text="Ваши увлечения:").pack(anchor="w")
hobby_music = tk.BooleanVar()
hobby_video = tk.BooleanVar()
hobby_drawing = tk.BooleanVar()

hobby_frame = tk.Frame(frame)
hobby_frame.pack(fill="x", pady=(5,10))
tk.Checkbutton(hobby_frame, text="Музыка", variable=hobby_music).pack(side="left", padx=10)
tk.Checkbutton(hobby_frame, text="Видео", variable=hobby_video).pack(side="left", padx=10)
tk.Checkbutton(hobby_frame, text="Рисование", variable=hobby_drawing).pack(side="left", padx=10)

tk.Label(frame, text="Ваша страна:").pack(anchor="w")
country_var = tk.StringVar()
country_combo = ttk.Combobox(frame, textvariable=country_var,
                             values=["Россия", "Украина", "Беларусь", "Казахстан"],
                             width=37)
country_combo.pack(fill="x", pady=(5,10))

tk.Label(frame, text="Ваш город:").pack(anchor="w")
entry_city = tk.Entry(frame, width=40)
entry_city.pack(fill="x", pady=(5,10))


tk.Label(frame, text="Кратко о себе:").pack(anchor="w")
text_about = tk.Text(frame, height=3, width=40)
text_about.pack(fill="x", pady=(5,5))
tk.Label(frame, text="краткая информация о ваших увлечениях",
         font=("Arial", 8), fg="gray").pack(anchor="w")


tk.Label(frame, text="Решите пример:").pack(anchor="w", pady=(10,0))
tk.Label(frame, text="3 + 4 = ?", font=("Arial", 10, "bold")).pack(anchor="w", pady=(5,5))
entry_math = tk.Entry(frame, width=40)
entry_math.pack(fill="x", pady=(0,15))


button_frame = tk.Frame(frame)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Отменить ввод", command=clear_form,
          width=15, bg="lightgray").pack(side="left", padx=5)
tk.Button(button_frame, text="Данные подтверждаю", command=submit_form,
          width=15, bg="lightgreen").pack(side="right", padx=5)
root.mainloop()
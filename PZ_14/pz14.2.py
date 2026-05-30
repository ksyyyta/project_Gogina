"""
Книжные магазины предлагают следующие коллекции книг.
Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
БукМаркет – Пушкин, Достоевский, Маяковский.
Галерея – Чехов, Тютчев, Пушкин. Определить в каких магазинах
можно приобрести книги Маяковского
"""
import tkinter as tk
from tkinter import messagebox

def calculate_distance():
    try:
        V1 = int(entry_v1.get())
        V2 = int(entry_v2.get())
        S = int(entry_s.get())
        T = int(entry_t.get())

        S1 = S + (V1 + V2)
        total_distance = S1 * T

        label_result.config(text=f"Расстояние между автомобилями через {T} часов: {total_distance} км")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число в каждое поле!")

root = tk.Tk()
root.title("Расчёт расстояния между автомобилями")
root.geometry("400x250")

tk.Label(root, text="Скорость первого автомобиля (км/ч):").pack(pady=5)
entry_v1 = tk.Entry(root)
entry_v1.pack()

tk.Label(root, text="Скорость второго автомобиля (км/ч):").pack(pady=5)
entry_v2 = tk.Entry(root)
entry_v2.pack()

tk.Label(root, text="Начальное расстояние между автомобилями (км):").pack(pady=5)
entry_s = tk.Entry(root)
entry_s.pack()

tk.Label(root, text="Время (ч):").pack(pady=5)
entry_t = tk.Entry(root)
entry_t.pack()
tk.Button(root, text="Рассчитать", command=calculate_distance, bg="lightblue").pack(pady=10)
label_result = tk.Label(root, text="", fg="green", font=("Arial", 10))
label_result.pack(pady=10)
root.mainloop()
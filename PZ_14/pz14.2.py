"""Скорость первого автомобиля V1 км/ч, второго — V2 км/ч, расстояние
между ними S км. Определить расстояние между ними через T часов, если автомобили
удаляются друг от друга. Данное расстояние равно сумме начального расстояния и общего
пути, проделанного автомобилями; общий путь = время • суммарная скорость."""
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
root.geometry("400x400")

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

import sqlite3
from data import initial_data  # Импортируем данные из файла data.py

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# Создаем таблицу, если её нет
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id_o TEXT PRIMARY KEY,
        price REAL,
        kol INTEGER,
        minz INTEGER
    )
''')

# Проверяем, есть ли уже данные в таблице, чтобы не дублировать их при каждом запуске
cursor.execute("SELECT COUNT(*) FROM orders")
count = cursor.fetchone()[0]

if count == 0:
    # Вставляем начальные данные только если таблица пуста
    try:
        cursor.executemany('''
            INSERT INTO orders (id_o, price, kol, minz)
            VALUES (?, ?, ?, ?)
        ''', initial_data)
        print("Начальные данные успешно добавлены.")
    except sqlite3.IntegrityError as e:
        print(f"Ошибка при вставке данных: {e}")
else:
    print("Данные уже существуют в базе, пропуск вставки.")

# Обновление цены
new_price = 199.99
target_id = '001'

cursor.execute("UPDATE orders SET price = ? WHERE id_o = ?", (new_price, target_id))
print(f"Цена товара {target_id} обновлена на {new_price}.")

conn.commit()

print("\nСписок товаров после обновления:")
cursor.execute('SELECT * FROM orders')
for row in cursor.fetchall():
    print(f"Код: {row[0]}, Цена: {row[1]} руб., На складе: {row[2]} шт., Мин. запас: {row[3]} шт.")

conn.close()
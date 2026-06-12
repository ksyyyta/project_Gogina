import sqlite3
from data import initial_data

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id_o TEXT PRIMARY KEY,
        price REAL,
        kol INTEGER,
        minz INTEGER
    )
''')

cursor.execute("SELECT COUNT(*) FROM orders")
count = cursor.fetchone()[0]

if count == 0:
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
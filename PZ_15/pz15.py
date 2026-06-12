"""
Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
источников в библиотеке. БД должна содержать таблицу Каталог с информацией о книгах
и следующей структурой записи: Код книги, Жанр, Страна издания, Серия, Автор,
Название книги, Год выпуска, Аннотация.
"""
import sqlite3 as sq
import os

DB = "library_v4.db"

def init_db():
    if os.path.exists(DB):
        os.remove(DB)
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE Catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            genre TEXT NOT NULL,
            country TEXT,
            series TEXT,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            year INTEGER,
            annotation TEXT
        )""")
        data = [
            ("Фантастика", "Россия", "Метро 2033", "Дмитрий Глуховский", "Метро 2033", 2005, "Постапокалипсис в метро."),
            ("Классика", "СССР", None, "Михаил Булгаков", "Мастер и Маргарита", 1967, "Роман  дьяволе и любви."),
            ("Детектив", "Великобритания", "Шерлок Холмс", "Артур Конан Дойл", "Собака Баскервилей", 1902, "Расследование в Англии."),
            ("НФ", "США", "Дюна", "Фрэнк Герберт", "Дюна", 1965, "Борьба за пустынную планету."),
            ("Поэзия", "Россия", None, "Александр Пушкин", "Евгений Онегин", 1833, "Роман в стихах."),
            ("Фэнтези", "Великобритания", "Властелин Колец", "Дж. Р. Р. Толкин", "Братство Кольца", 1954, "Эпическое фэнтези."),
            ("Исторический", "Франция", None, "Александр Дюма", "Три мушкетера", 1844, "Приключения гвардейцев."),
            ("Философия", "Германия", None, "Фридрих Ницше", "Так говорил Заратустра", 1883, "Философская притча."),
            ("Сказка", "Дания", None, "Ганс Христиан Андерсен", "Дюймовочка", 1835, "История маленькой девочки."),
            ("Триллер", "США", None, "Стивен Кинг", "Сияние", 1977, "Ужасы в отеле.")
        ]
        cur.executemany("INSERT INTO Catalog (genre, country, series, author, title, year, annotation) VALUES (?,?,?,?,?,?,?)", data)

def search_by_author():
    author = input("Поиск по автору: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Catalog WHERE author LIKE ?", (f"%{author}%",))
        for i in cur:
            print(i)

def search_by_genre_year():
    genre = input("Жанр: ")
    try:
        start_year = int(input("Год от: "))
        end_year = int(input("Год до: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Catalog WHERE genre = ? AND year BETWEEN ? AND ?", (genre, start_year, end_year))
            for i in cur:
                print(i)
    except ValueError:
        print("Некорректный год.")

def search_by_title():
    title = input("Поиск по названию: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Catalog WHERE title LIKE ?", (f"%{title}%",))
        for i in cur:
            print(i)

def edit_annotation():
    bid = int(input("ID книги: "))
    new_ann = input("Новая аннотация: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Catalog SET annotation = ? WHERE id = ?", (new_ann, bid))
        print("Аннотация обновлена." if cur.rowcount else "Не найдено.")

def edit_year():
    author = input("Автор для изменения года: ")
    new_year = int(input("Новый год выпуска: "))
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Catalog SET year = ? WHERE author = ?", (new_year, author))
        print(f"Обновлено записей: {cur.rowcount}")

def edit_series():
    genre = input("Жанр: ")
    country = input("Страна: ")
    new_series = input("Новая серия: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Catalog SET series = ? WHERE genre = ? AND country = ?", (new_series, genre, country))
        print(f"Обновлено записей: {cur.rowcount}")

def delete_by_id():
    bid = int(input("ID книги для удаления: "))
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Catalog WHERE id = ?", (bid,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_old_year():
    year = int(input("Удалить книги старше года: "))
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Catalog WHERE year < ?", (year,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_genre():
    genre = input("Удалить жанр: ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Catalog WHERE genre = ?", (genre,))
        print(f"Удалено записей: {cur.rowcount}")

init_db()

while True:
    print("\n=== МЕНЮ БИБЛИОТЕКА ===")
    print("1 - Показать все книги")
    print("2 - Поиск по автору")
    print("3 - Поиск по жанру и годам")
    print("4 - Поиск по названию")
    print("5 - Изменить аннотацию")
    print("6 - Изменить год выпуска автора")
    print("7 - Изменить серию по жанру/стране")
    print("8 - Удалить по ID")
    print("9 - Удалить старые книги")
    print("10 - Удалить по жанру")
    print("0 - Выход")

    cmd = input("Выберите: ")

    if cmd == '1':
        with sq.connect(DB) as con:
            for i in con.cursor().execute("SELECT * FROM Catalog"):
                print(i)
    elif cmd == '2':
        search_by_author()
    elif cmd == '3':
        search_by_genre_year()
    elif cmd == '4':
        search_by_title()
    elif cmd == '5':
        edit_annotation()
    elif cmd == '6':
        edit_year()
    elif cmd == '7':
        edit_series()
    elif cmd == '8':
        delete_by_id()
    elif cmd == '9':
        delete_by_old_year()
    elif cmd == '10':
        delete_by_genre()
    elif cmd == '0':
        break
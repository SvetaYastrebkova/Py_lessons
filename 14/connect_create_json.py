import pathlib
import sqlite3
import json

# Путь к базе данных
SQLITE_DATABASE = pathlib.Path(__file__).parent.joinpath("Database", "my_test_db.db")

# SQL-запрос для создания таблицы
SQL_CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    course TEXT
)
'''

# Загружаем данные из JSON
# Пример содержимого students.json:
# [
#   {"first_name":"Karim","last_name":"Clem","email":"kclem0@hexun.com","course":"Python"},
#   {"first_name":"Anna","last_name":"Smith","email":"asmith@mail.com","course":"Data Science"}
# ]
json_file = pathlib.Path(__file__).parent.joinpath("students.json")
with open(json_file, "r", encoding="utf-8") as f:
    students_data = json.load(f)

# Работа с базой
with sqlite3.connect(SQLITE_DATABASE) as conn:
    cursor = conn.cursor()
    # Создание таблицы
    cursor.execute(SQL_CREATE_TABLE)

    # Вставка данных
    for student in students_data:
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, course) VALUES (?, ?, ?, ?)",
            (student["first_name"], student["last_name"], student["email"], student["course"])
        )
    conn.commit()

print("Данные успешно загружены в таблицу students!")

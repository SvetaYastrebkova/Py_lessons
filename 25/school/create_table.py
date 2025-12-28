import sqlite3

DB_NAME = "school.db"

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Таблица групп
    c.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT NOT NULL,
        teacher_name TEXT NOT NULL,
        max_students INTEGER NOT NULL
    )
    """)

    # Таблица студентов
    c.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        balance REAL DEFAULT 0.0,
        group_id INTEGER,
        FOREIGN KEY(group_id) REFERENCES groups(id)
    )
    """)

    # Таблица курсов
    c.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT UNIQUE NOT NULL
    )
    """)

    # Связующая таблица группа ↔ курс
    c.execute("""
    CREATE TABLE IF NOT EXISTS group_courses (
        group_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY(group_id, course_id),
        FOREIGN KEY(group_id) REFERENCES groups(id),
        FOREIGN KEY(course_id) REFERENCES courses(id)
    )
    """)

    conn.commit()
    conn.close()
    print(f"✅ База данных '{DB_NAME}' и таблицы успешно созданы.")

if __name__ == "__main__":
    create_tables()

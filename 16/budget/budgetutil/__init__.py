import os
import sqlite3
from .const import DB_FILE, TABLE_CATEGORIES, TABLE_TRANSACTIONS

def init_db():
    """Создание БД и таблиц, если они не существуют"""
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_CATEGORIES} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    """)

    cur.execute(f"""
    CREATE TABLE IF NOT EXISTS {TABLE_TRANSACTIONS} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        amount REAL NOT NULL,
        sign TEXT CHECK(sign IN ('+','-')) NOT NULL,
        balance REAL NOT NULL,
        category_id INTEGER,
        comment TEXT,
        FOREIGN KEY(category_id) REFERENCES {TABLE_CATEGORIES}(id)
    )
    """)

    conn.commit()
    conn.close()

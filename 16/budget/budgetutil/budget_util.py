import sqlite3
import os
import csv
from pathlib import Path
from .const import DB_FILE, TABLE_TRANSACTIONS, TABLE_CATEGORIES

def add_transaction(date, amount, sign, category, comment=""):
    """Добавить транзакцию и пересчитать баланс"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    # Проверка категории
    cur.execute(f"SELECT id FROM {TABLE_CATEGORIES} WHERE name=?", (category,))
    row = cur.fetchone()
    if row:
        category_id = row[0]
    else:
        cur.execute(f"INSERT INTO {TABLE_CATEGORIES}(name) VALUES (?)", (category,))
        category_id = cur.lastrowid

    # Последний баланс
    cur.execute(f"SELECT balance FROM {TABLE_TRANSACTIONS} ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    last_balance = row[0] if row else 0

    new_balance = last_balance + amount if sign == "+" else last_balance - amount

    # Добавляем запись
    cur.execute(f"""
    INSERT INTO {TABLE_TRANSACTIONS}(date, amount, sign, balance, category_id, comment)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (date, amount, sign, new_balance, category_id, comment))

    conn.commit()
    conn.close()


def get_balance():
    """Получить текущий баланс"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(f"SELECT balance FROM {TABLE_TRANSACTIONS} ORDER BY id DESC LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return row[0] if row else 0


def export_transactions(filename: str = None):
    """Экспорт транзакций в CSV"""
    # Если filename не указан, кладём файл в budget_reports в корне проекта
    if filename is None:
        BASE_DIR = Path(__file__).resolve().parent.parent
        REPORTS_DIR = BASE_DIR / "budget_reports"
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        filename = REPORTS_DIR / "transactions.csv"
    else:
        filename = Path(filename)
        filename.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(f"""
    SELECT t.id, t.date, t.amount, t.sign, t.balance, c.name, t.comment
    FROM {TABLE_TRANSACTIONS} t
    LEFT JOIN {TABLE_CATEGORIES} c ON t.category_id = c.id
    ORDER BY t.id
    """)

    rows = cur.fetchall()
    conn.close()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Date", "Amount", "Sign", "Balance", "Category", "Comment"])
        writer.writerows(rows)

    return str(filename)

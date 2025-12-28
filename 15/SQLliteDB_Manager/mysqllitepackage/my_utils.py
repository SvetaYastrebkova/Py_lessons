#my utils

import sqlite3
import pathlib
import os
import json

# --- Работа с БД и таблицами ---


def create_database(db_name: str) -> str:
    """Создать новую БД (если нет). Возвращает путь."""
    db_path = pathlib.Path(db_name)
    if not db_path.exists():
        conn = sqlite3.connect(db_path)
        conn.close()
    return str(db_path)

def delete_database(db_name: str) -> None:
    """Удалить файл базы данных."""
    db_path = pathlib.Path(db_name)
    if db_path.exists():
        os.remove(db_path)

def create_table(db_name: str, create_table_sql: str) -> None:
    """Создать таблицу по SQL-запросу."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()

def delete_table(db_name: str, table_name: str) -> None:
    """Удалить таблицу."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()

def alter_table(db_name: str, alter_sql: str) -> None:
    """Изменить структуру таблицы."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(alter_sql)
        conn.commit()


# --- CRUD для данных таблицы ---


def add_record(db_name: str, insert_sql: str, values: tuple) -> None:
    """Добавить запись."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(insert_sql, values)
        conn.commit()

def read_records(db_name: str, select_sql: str) -> list:
    """Прочитать записи и вернуть список кортежей."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        result = cursor.execute(select_sql).fetchall()
    return result

def update_record(db_name: str, update_sql: str, values: tuple) -> None:
    """Обновить запись."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(update_sql, values)
        conn.commit()

def delete_record(db_name: str, delete_sql: str, values: tuple) -> None:
    """Удалить запись."""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(delete_sql, values)
        conn.commit()
        
        
# Импортировать данные из JSON в таблицу
def import_json_to_table(db_name: str, table_name: str, json_file: str) -> None:
    """Импортировать данные из JSON в таблицу. Создаёт таблицу, если нет."""
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)  # JSON -> список словарей

    if not isinstance(data, list) or not data:
        raise ValueError("JSON должен содержать непустой список объектов")

    # формируем список колонок (по ключам из первого словаря)
    columns = list(data[0].keys())
    col_defs = ", ".join(f"{col} TEXT" for col in columns)  # все TEXT для простоты

    # создаём таблицу, если не существует
    create_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({col_defs})"
    
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(create_sql)
        
        placeholders = ", ".join(["?" for _ in columns])
        col_names = ", ".join(columns)
        sql = f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"

        # вставляем все записи
        for record in data:
            values = tuple(record[col] for col in columns)
            cursor.execute(sql, values)

        conn.commit()
    print(f"Импортировано {len(data)} записей из {json_file} в таблицу {table_name}")

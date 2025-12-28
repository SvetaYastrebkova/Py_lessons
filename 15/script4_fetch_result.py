import pathlib
import sqlite3


SQLITE_DATABASE = pathlib.Path(__file__).parent.joinpath("Database","my_db.db")
TABLE_NAME = 'employees'
SQL_SELECT_ALL = f'''
SELECT * FROM {TABLE_NAME}
WHERE gender = 'Female';
'''

with sqlite3.connect(SQLITE_DATABASE) as conn:
    # Create Cursor object -> to operate with DB
    cursor = conn.cursor()
    query_result = cursor.execute(SQL_SELECT_ALL).fetchall()
    pass

print(type(query_result))
print(len(query_result))
print(type(query_result[0]))
print(len(query_result[0]))
print(query_result[0])


print(f"Найдено записей: {len(query_result)}")
print(query_result[:5])  # выведем первые 5 для примера

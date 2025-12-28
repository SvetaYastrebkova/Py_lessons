
import pathlib
import sqlite3


SQLITE_DATABASE = pathlib.Path(__file__).parent.joinpath("Database","my_test_db.db")
SQL_CREATE_TABLE = '''
CREATE TABLE "users" (
	"id"	INTEGER,
	"name"	TEXT,
	"email"	TEXT,
	"employment_date"	TEXT
);
'''

# with block -> recommended!!
with sqlite3.connect(SQLITE_DATABASE) as conn:
    # Create Cursor object -> to operate with DB
    cursor = conn.cursor()
    cursor.execute(SQL_CREATE_TABLE)
    pass

import pathlib
import sqlite3


SQLITE_DATABASE = pathlib.Path(__file__).parent.joinpath("Database", "my_test_db.db")
USERS_LIST = [
    ["1", "Beatrix", "bsmallpeice0@netlog.com", "8/5/2025"],
    ["2", "Giovanna", "gtickel1@seesaa.net", "9/15/2024"],
    ["3", "Mick", "mmahedy2@csmonitor.com", "10/10/2024"],
    ["4", "Estell", "egranleese3@squarespace.com", "2/17/2025"],
]
SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER,
	"name"	TEXT,
	"email"	TEXT,
	"employment_date"	TEXT
);
"""
SQL_ADD_USERS_RECORD = '''
INSERT INTO "users"
("id","name","email","employment_date") 
VALUES 
('{}','{}','{}','{}');

'''

# with block -> recommended!!
with sqlite3.connect(SQLITE_DATABASE) as conn:
    # Create Cursor object -> to operate with DB
    cursor = conn.cursor()
    cursor.execute(SQL_CREATE_TABLE) # create table if not exists
    for u in USERS_LIST:
        print(SQL_ADD_USERS_RECORD.format(*u))
        cursor.execute(SQL_ADD_USERS_RECORD.format(*u))

        pass
    cursor.close()    
    pass

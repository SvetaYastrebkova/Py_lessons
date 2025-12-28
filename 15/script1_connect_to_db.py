
import pathlib
import sqlite3


SQLITE_DATABASE = pathlib.Path(__file__).parent.joinpath("Database","my_db.db")

# Create Connection object
connection = sqlite3.connect(SQLITE_DATABASE)

# Create Cursor object -> to operate with DB
cursor = connection.cursor()

# with block -> recommended!!
with sqlite3.connect(SQLITE_DATABASE) as conn:
    # Create Cursor object -> to operate with DB
    cursor = conn.cursor()
    pass

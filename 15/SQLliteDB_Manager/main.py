#main py
import mysqllitepackage.my_utils


DB_FILE = "test.db"

MAIN_MENU = '''Select:
0 - Exit
1 - Create DB
2 - Create Table
3 - Add Record
4 - Read Records1
5 - Update Record
6 - Delete Record
7 - Delete Table
8 - Delete DB
9 - Import JSON
'''

if __name__ == "__main__":
    while True:
        choice = input(MAIN_MENU)

        if choice == "0":
            print("Bye!")
            break

        elif choice == "1":
            mysqllitepackage.my_utils.create_database(DB_FILE)
            print("Database created!")

        elif choice == "2":
            sql = '''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT
            )
            '''
            mysqllitepackage.my_utils.create_table(DB_FILE, sql)
            print("Table created!")

        elif choice == "3":
            name = input("Name: ")
            email = input("Email: ")
            sql = "INSERT INTO employees (name, email) VALUES (?, ?)"
            mysqllitepackage.my_utils.add_record(DB_FILE, sql, (name, email))
            print("Record added!")

        elif choice == "4":
            sql = "SELECT * FROM employees"
            rows = mysqllitepackage.my_utils.read_records(DB_FILE, sql)
            for row in rows:
                print(row)

        elif choice == "5":
            emp_id = int(input("Employee ID: "))
            new_email = input("New email: ")
            sql = "UPDATE employees SET email = ? WHERE id = ?"
            mysqllitepackage.my_utils.update_record(DB_FILE, sql, (new_email, emp_id))
            print("Record updated!")

        elif choice == "6":
            emp_id = int(input("Employee ID: "))
            sql = "DELETE FROM employees WHERE id = ?"
            mysqllitepackage.my_utils.delete_record(DB_FILE, sql, (emp_id,))
            print("Record deleted!")

        elif choice == "7":
            mysqllitepackage.my_utils.delete_table(DB_FILE, "employees")
            print("Table deleted!")

        elif choice == "8":
            mysqllitepackage.my_utils.delete_database(DB_FILE)
            print("Database deleted!")

        elif choice == "9":
            json_file = input("Введите путь к JSON: ")
            mysqllitepackage.my_utils.import_json_to_table(DB_FILE, "employees", json_file)

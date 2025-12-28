import sqlite3

DB_NAME = "school.db"

# ==================== CLASS Student ====================
class Student:
    def __init__(self, first_name, last_name, email, balance=0.0, group_id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.balance = balance
        self.group_id = group_id

    def add_balance(self, amount):
        self.balance += amount
        print(f"💰 {self.first_name} {self.last_name} баланс пополнен на {amount}. Новый баланс: {self.balance}")

    def pay(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"✅ {self.first_name} {self.last_name} оплатил {amount}. Остаток: {self.balance}")
        else:
            print(f"❌ Недостаточно средств для {self.first_name} {self.last_name}")

# ==================== CLASS Group ====================
class Group:
    def __init__(self, group_name, teacher_name, max_students):
        self.group_name = group_name
        self.teacher_name = teacher_name
        self.max_students = max_students

# ==================== CLASS School ====================
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.conn = sqlite3.connect(DB_NAME)
        self.create_tables()

    def create_tables(self):
        c = self.conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT,
            teacher_name TEXT,
            max_students INTEGER
        )""")
        c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            email TEXT UNIQUE,
            balance REAL DEFAULT 0.0,
            group_id INTEGER,
            FOREIGN KEY(group_id) REFERENCES groups(id)
        )""")
        c.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT UNIQUE
        )""")
        c.execute("""
        CREATE TABLE IF NOT EXISTS group_courses (
            group_id INTEGER,
            course_id INTEGER,
            PRIMARY KEY(group_id, course_id),
            FOREIGN KEY(group_id) REFERENCES groups(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )""")
        self.conn.commit()

    # ================= CRUD Students =================
    def add_student(self, student: Student):
        c = self.conn.cursor()
        c.execute("INSERT INTO students (first_name, last_name, email, balance, group_id) VALUES (?, ?, ?, ?, ?)",
                  (student.first_name, student.last_name, student.email, student.balance, student.group_id))
        self.conn.commit()
        print(f"✅ Студент {student.first_name} {student.last_name} добавлен")

    def get_student(self, email):
        c = self.conn.cursor()
        c.execute("SELECT * FROM students WHERE email=?", (email,))
        return c.fetchone()

    def update_student_balance(self, email, amount):
        c = self.conn.cursor()
        c.execute("UPDATE students SET balance = balance + ? WHERE email=?", (amount, email))
        self.conn.commit()

    def delete_student(self, email):
        c = self.conn.cursor()
        c.execute("DELETE FROM students WHERE email=?", (email,))
        self.conn.commit()
        print(f"🗑 Студент с email {email} удален")

    # ================= CRUD Groups =================
    def add_group(self, group: Group):
        c = self.conn.cursor()
        c.execute("INSERT INTO groups (group_name, teacher_name, max_students) VALUES (?, ?, ?)",
                  (group.group_name, group.teacher_name, group.max_students))
        self.conn.commit()
        print(f"✅ Группа {group.group_name} добавлена")

    def list_students_in_group(self, group_id):
        c = self.conn.cursor()
        c.execute("SELECT first_name, last_name, email FROM students WHERE group_id=?", (group_id,))
        return c.fetchall()

# ==================== Example ====================
if __name__ == "__main__":
    school = School("Haifa Tech School", "Haifa, Israel")

    # Создание группы
    g1 = Group("Cloud Computing", "Mr. Cohen", 30)
    school.add_group(g1)

    # Добавление студента
    s1 = Student("Way", "Oda", "woda0@smugmug.com", 275.5, group_id=1)
    school.add_student(s1)

    # Обновление баланса
    school.update_student_balance("woda0@smugmug.com", 100)

    # Вывод студентов группы
    students_in_group = school.list_students_in_group(1)
    print("📋 Студенты группы Cloud Computing:", students_in_group)

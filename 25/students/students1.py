import csv

class Student:
    def __init__(self, first_name, last_name, email, gender, course, balance=0.0):
        """
        Конструктор класса Student.
        Создаёт нового студента с указанными характеристиками.
        """
        self.first_name = first_name      # имя
        self.last_name = last_name        # фамилия
        self.email = email                # адрес электронной почты
        self.gender = gender              # пол ("male"/"female"/"other")
        self.course = course              # текущий курс
        self.balance = balance            # баланс студента (число)


    def full_name(self):
        """
        Возвращает полное имя
        """
        return f"{self.first_name} {self.last_name}"

    def add_balance(self, amount):
        """
        Пополняет баланс студента.
        """
        if amount > 0:
            self.balance += amount
            print(f"[{self.full_name()}] Баланс пополнен на {amount:.2f}. Новый баланс: {self.balance:.2f}")
        else:
            print("Сумма пополнения должна быть положительной.")

    def pay(self, amount):
        """
        Списывает средства с баланса при оплате.
        """
        if amount <= 0:
            print(" Сумма оплаты должна быть положительной.")
            return

        if self.balance >= amount:
            self.balance -= amount
            print(f"[{self.full_name()}]  Оплата {amount:.2f} выполнена. Остаток на балансе: {self.balance:.2f}")
        else:
            print(f" [{self.full_name()}]  Недостаточно средств. Текущий баланс: {self.balance:.2f}")

    def change_course(self, new_course):
        """
        Меняет курс студента.
        """
        if new_course != self.course:
            print(f"[{self.full_name()}]  Курс изменён с '{self.course}' на '{new_course}'.")
            self.course = new_course
        else:
            print(f"[{self.full_name()}]  Студент уже обучается на курсе '{self.course}'.")

    def info(self):
        """
        Выводит подробную информацию о студенте.
        """
        print(f"""
Информация о студенте:
Имя: {self.first_name} {self.last_name}
Пол: {self.gender}
Email: {self.email}
Курс: {self.course}
Баланс: {self.balance:.2f}
""")



def load_students_from_csv(filename):
    """
    Загружает студентов из CSV-файла и возвращает список объектов Student.
    """
    students = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = Student(
                first_name=row['first_name'],
                last_name=row['last_name'],
                email=row['email'],
                gender=row['gender'],
                course=row['course'],
                balance=float(row['balance']) if row['balance'] else 0.0
            )
            students.append(student)
    return students

'''
# Создание студентов
s1 = Student("Anna", "Cohen", "anna@example.com", "female", "Python for Beginners", 100.0)
s2 = Student("David", "Levi", "david@example.com", "male", "Kubernetes Fundamentals", 50.0)
'''

# === Пример использования ===
students = load_students_from_csv("students_data.csv")

print(f" Загружено студентов: {len(students)}\n")

# Вывод первых трёх студентов
for s in students[:3]:
    s.info()
# вывод конкретного студента в списке
students[5].info()
# Пример операций
students[0].add_balance(100)
students[1].change_course("DevOps Cloud")
students[2].pay(50)
students[1].change_course("DevOps Cloud")
students[4].change_course("DevOps Cloud")
students[5].change_course("DevOps Cloud")

students[5].info()

'''
# Пополнение и оплата
s1.add_balance(50)
s1.pay(80)

# Изменение курса
s2.change_course("Cloud DevOps")

# Печать информации
s1.info()
s2.info()
'''
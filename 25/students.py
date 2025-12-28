class Student:
    
    def __init__(self, name, student_id, email):
        """
        Конструктор — вызывается при создании нового объекта Student.
        Инициализирует основные характеристики студента.
        """
        self.name = name                  # имя студента
        self.student_id = student_id      # уникальный ID
        self.email = email                # e-mail
        self.courses = []                 # список курсов, изначально пуст
        self.payment_status = False       # статус оплаты: False = не оплачено
        
    def add_course(self, course_name):
        """
        Добавляет новый курс студенту.
        """
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"✅ Курс '{course_name}' добавлен студенту {self.name}.")
        else:
            print(f"⚠️ Курс '{course_name}' уже назначен студенту {self.name}.")
            
    def set_payment_status(self, status: bool):
        """
        Устанавливает статус оплаты (True — оплачено, False — не оплачено).
        """
        self.payment_status = status
        print(f"💰 Статус оплаты для {self.name}: {'оплачено' if status else 'не оплачено'}.")
        
    def info(self):
        """
        Выводит краткую информацию о студенте.
        """
        print(f"""
📄 Информация о студенте:
Имя: {self.name}
ID: {self.student_id}
Email: {self.email}
Курсы: {', '.join(self.courses) if self.courses else 'нет курсов'}
Оплата: {'оплачено' if self.payment_status else 'не оплачено'}
""")



# Создаём студентов
s1 = Student("Anna Cohen", "ST123", "anna@example.com")
s2 = Student("David Levi", "ST456", "david@example.com")

# Добавляем курсы
s1.add_course("Python Basics")
s1.add_course("Cloud DevOps")
s2.add_course("Kubernetes Fundamentals")

# Изменяем статус оплаты
s1.set_payment_status(True)
s2.set_payment_status(False)

# Выводим информацию
s1.info()
s2.info()

from students1 import load_students_from_csv

def show_menu():
    print("\n МЕНЮ:")
    print("1. Показать всех студентов")
    print("2. Показать информацию о студенте")
    print("3. Пополнить баланс")
    print("4. Изменить курс")
    print("5. Оплатить")
    print("0. Выйти")

def find_student(students, email):
    for s in students:
        if s.email.lower() == email.lower():
            return s
    return None

def main():
    students = load_students_from_csv("students_data.csv")
    print(f" Загружено студентов: {len(students)}")

    while True:
        show_menu()
        choice = input(" Выберите действие: ").strip()

        if choice == "0":
            print(" До свидания!")
            break

        elif choice == "1":
            print("\n=== Список студентов ===")
            for s in students[:10]:  # ограничим вывод первыми 10 для примера
                print(f"{s.first_name} {s.last_name} | {s.course} | Баланс: {s.balance}")
            print("... (показаны первые 10 студентов)")

        elif choice == "2":
            email = input("Введите email студента: ").strip()
            student = find_student(students, email)
            if student:
                student.info()
            else:
                print(" Студент не найден.")

        elif choice == "3":
            email = input("Введите email студента: ").strip()
            student = find_student(students, email)
            if student:
                try:
                    amount = float(input("Введите сумму пополнения: "))
                    student.add_balance(amount)
                except ValueError:
                    print(" Ошибка: введите число.")
            else:
                print(" Студент не найден.")

        elif choice == "4":
            email = input("Введите email студента: ").strip()
            student = find_student(students, email)
            if student:
                new_course = input("Введите новый курс: ").strip()
                student.change_course(new_course)
            else:
                print(" Студент не найден.")

        elif choice == "5":
            email = input("Введите email студента: ").strip()
            student = find_student(students, email)
            if student:
                try:
                    amount = float(input("Введите сумму оплаты: "))
                    student.pay(amount)
                except ValueError:
                    print(" Ошибка: введите число.")
            else:
                print(" Студент не найден.")

        else:
            print(" Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

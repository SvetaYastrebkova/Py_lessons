from school import School, Student, Group

def show_menu():
    print("\n🎓 МЕНЮ ШКОЛЫ")
    print("1. Показать всех студентов")
    print("2. Добавить студента")
    print("3. Удалить студента")
    print("4. Добавить баланс студенту")
    print("5. Создать группу")
    print("6. Показать студентов группы")
    print("0. Выйти")

def main():
    school = School("Haifa Tech School", "Haifa, Israel")
    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()

        if choice == "0":
            print("👋 До свидания!")
            break

        elif choice == "1":
            c = school.conn.cursor()
            c.execute("SELECT first_name, last_name, email, balance, group_id FROM students")
            students = c.fetchall()
            print("\n📋 Все студенты:")
            for s in students:
                print(f"{s[0]} {s[1]} | Email: {s[2]} | Баланс: {s[3]:.2f} | Group ID: {s[4]}")

        elif choice == "2":
            first_name = input("Имя: ").strip()
            last_name = input("Фамилия: ").strip()
            email = input("Email: ").strip()
            balance = float(input("Баланс: ").strip() or 0.0)
            group_id = input("Group ID (оставьте пустым если нет): ").strip()
            group_id = int(group_id) if group_id else None
            student = Student(first_name, last_name, email, balance, group_id)
            school.add_student(student)

        elif choice == "3":
            email = input("Email студента для удаления: ").strip()
            school.delete_student(email)

        elif choice == "4":
            email = input("Email студента: ").strip()
            amount = float(input("Сумма для добавления: ").strip())
            school.update_student_balance(email, amount)
            print(f"💰 Баланс обновлён для {email}")

        elif choice == "5":
            group_name = input("Название группы: ").strip()
            teacher_name = input("Имя преподавателя: ").strip()
            max_students = int(input("Макс. количество студентов: ").strip())
            group = Group(group_name, teacher_name, max_students)
            school.add_group(group)

        elif choice == "6":
            group_id = int(input("ID группы: ").strip())
            students = school.list_students_in_group(group_id)
            print(f"\n📋 Студенты группы {group_id}:")
            for s in students:
                print(f"{s[0]} {s[1]} | Email: {s[2]}")

        else:
            print("❌ Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

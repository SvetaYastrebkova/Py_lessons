from pathlib import Path
import json

# путь к JSON-файлу
file_path = Path(__file__).parent / "users.json"

# функция для загрузки данных
def load_data():
    if file_path.exists():
        with file_path.open(encoding="utf-8") as f:
            return json.load(f)
    return []

# функция для сохранения данных
def save_data(data):
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# показать всех пользователей
def list_users(data):
    for i, user in enumerate(data, start=1):
        print(f"{i}. {user['name']} | {user['email']} | {user['gender']} | {user.get('address')}")

# добавить пользователя
def add_user(data):
    name = input("Имя: ")
    email = input("Email: ")
    password = input("Пароль: ")
    gender = input("Пол: ")
    address = input("Адрес (можно оставить пустым): ")
    address = address if address else None
    data.append({
        "name": name,
        "email": email,
        "password": password,
        "gender": gender,
        "address": address
    })
    save_data(data)
    print("Пользователь добавлен!")

# обновить пользователя
def update_user(data):
    list_users(data)
    idx = int(input("Введите номер пользователя для редактирования: ")) - 1
    if 0 <= idx < len(data):
        user = data[idx]
        print("Оставьте пустым, чтобы не менять значение.")
        name = input(f"Имя [{user['name']}]: ") or user['name']
        email = input(f"Email [{user['email']}]: ") or user['email']
        password = input(f"Пароль [{user['password']}]: ") or user['password']
        gender = input(f"Пол [{user['gender']}]: ") or user['gender']
        address = input(f"Адрес [{user.get('address')}]: ") or user.get('address')
        data[idx] = {
            "name": name,
            "email": email,
            "password": password,
            "gender": gender,
            "address": address
        }
        save_data(data)
        print("Пользователь обновлен!")
    else:
        print("Неверный номер.")

# удалить пользователя
def delete_user(data):
    list_users(data)
    idx = int(input("Введите номер пользователя для удаления: ")) - 1
    if 0 <= idx < len(data):
        user = data.pop(idx)
        save_data(data)
        print(f"Пользователь {user['name']} удален!")
    else:
        print("Неверный номер.")

# главное меню
def main():
    data = load_data()
    while True:
        print("\nВыберите действие: ")
        print("1 - Показать всех пользователей")
        print("2 - Добавить пользователя")
        print("3 - Обновить пользователя")
        print("4 - Удалить пользователя")
        print("0 - Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            list_users(data)
        elif choice == "2":
            add_user(data)
        elif choice == "3":
            update_user(data)
        elif choice == "4":
            delete_user(data)
        elif choice == "0":
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()

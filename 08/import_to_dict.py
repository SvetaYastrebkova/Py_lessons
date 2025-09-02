from pathlib import Path

# Определяем путь к файлу
file_path = Path(__file__).parent / "users.csv"

users = {}

with file_path.open(encoding="utf-8") as f:
    lines = f.read().strip().splitlines()

# первая строка — заголовки
headers = lines[0].split(",")

for line in lines[1:]:
    values = line.split(",")
    row = dict(zip(headers, values))
    user_id = int(row["id"])
    users[user_id] = {
        "first_name": row["first_name"],
        "last_name": row["last_name"],
        "email": row["email"],
        "gender": row["gender"],
        "ip_address": row["ip_address"]
    }

# проверим результат
for uid, data in users.items():
    print(uid, "→", data)

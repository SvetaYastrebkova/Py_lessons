from pathlib import Path
import json

# путь к файлу в той же папке, что и скрипт
file_path = Path(__file__).parent / "data.json"

# проверяем, существует ли файл
if not file_path.exists():
    print(f"Файл не найден: {file_path}")
else:
    with file_path.open(encoding="utf-8") as f:
        data = json.load(f)
    print(data)


#  структура JSON такая:
# {
#   "rates": {
#       "USD": 1.0,
#       "EUR": 0.91,
#       "ILS": 3.45
#   }
# }


# читаем JSON
with file_path.open(encoding="utf-8") as f:
    data = json.load(f)


ils_rate = data["rates"].get("ILS")  # получаем курс ILS
print("ILS rate:", ils_rate)


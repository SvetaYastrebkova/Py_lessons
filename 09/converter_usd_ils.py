from pathlib import Path
import json

# путь к файлу в той же папке, что и скрипт
file_path = Path(__file__).parent / "data.json"

# проверяем, существует ли файл
if not file_path.exists():
    print(f"Файл не найден: {file_path}")
    exit(1)

# читаем JSON
with file_path.open(encoding="utf-8") as f:
    data = json.load(f)
    
#  структура JSON такая:
# {
#   "rates": {
#       "USD": 1.0,
#       "EUR": 0.91,
#       "ILS": 3.45
#   }
# }


# получаем курс ILS
ils_rate = data.get("rates", {}).get("ILS")
if ils_rate is None:
    print("ILS rate не найден в файле")
    exit(1)

print(f"Текущий курс USD → ILS: {ils_rate} ₪ за 1 USD")

# вводим сумму в долларах
try:
    usd_amount = float(input("Введите сумму в USD: "))
except ValueError:
    print("Неверный ввод!")
    exit(1)

# конвертация
ils_amount = usd_amount * ils_rate
print(f"{usd_amount} USD = {ils_amount:.2f} ₪")

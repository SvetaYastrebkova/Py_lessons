from pathlib import Path
import json
import requests
from datetime import datetime

# путь к локальному файлу
file_path = Path(__file__).parent / "data.json"
log_file = Path(__file__).parent / "log_converter.log"

# функция для записи логов
def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with log_file.open("a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

# функция получения курса USD → target_currency через Frankfurter API
def get_rate(target_currency: str):
    url = f"https://api.frankfurter.app/latest?from=USD&to={target_currency.upper()}"
    try:
        log(f"Запрашиваем курс {target_currency} через Frankfurter API")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data.get("rates", {}).get(target_currency.upper())

        if rate is None:
            raise ValueError(f"API не вернул курс {target_currency}")

        log(f"Получен курс {target_currency} через API: {rate}")
        # сохраняем весь ответ в файл
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        log("Курсы сохранены в локальный файл")
        return rate

    except Exception as e:
        log(f"Ошибка при запросе API: {e}")
        # пробуем локальный файл
        if file_path.exists():
            try:
                with file_path.open(encoding="utf-8") as f:
                    data = json.load(f)
                rate = data.get("rates", {}).get(target_currency.upper())
                if rate is not None:
                    log(f"Курс {target_currency} взят из локального файла")
                    return rate
                else:
                    log(f"В локальном файле нет курса {target_currency}")
            except Exception as fe:
                log(f"Ошибка при чтении локального файла: {fe}")

        raise RuntimeError(f"Не удалось получить курс {target_currency}")

# --- основная программа ---
currency = input("Введите код валюты (например, ILS, EUR, RUB): ").strip().upper()

try:
    rate = get_rate(currency)
    print(f"Текущий курс USD → {currency}: {rate} {currency} за 1 USD")
except Exception as e:
    print("Ошибка: не удалось получить курс.")
    log(f"Критическая ошибка: {e}")
    exit(1)

# ввод суммы
try:
    usd_amount = float(input("Введите сумму в USD: "))
    log(f"Пользователь ввел сумму: {usd_amount} USD")
except ValueError:
    log("Пользователь ввел некорректное значение")
    print("Неверный ввод!")
    exit(1)

# конвертация
converted = usd_amount * rate
print(f"{usd_amount} USD = {converted:.2f} {currency}")
log(f"Конвертировано: {usd_amount} USD = {converted:.2f} {currency}")

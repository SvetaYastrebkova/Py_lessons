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

# функция для получения курса USD → ILS
def get_ils_rate():
    url = "https://api.exchangerate.host/latest?base=USD&symbols=ILS"
    try:
        log("Запрашиваем курс ILS через API")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data.get("rates", {}).get("ILS")

        if rate is None:
            raise ValueError("API вернуло пустой курс ILS")

        log(f"Получен курс ILS через API: {rate}")
        # сохраняем в файл для fallback
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        log("Курс сохранен в локальный файл")
        return rate

    except Exception as e:
        log(f"Ошибка при запросе API: {e}")
        # пробуем локальный файл
        if file_path.exists():
            try:
                with file_path.open(encoding="utf-8") as f:
                    data = json.load(f)
                rate = data.get("rates", {}).get("ILS")
                if rate is not None:
                    log("Курс ILS взят из локального файла")
                    return rate
                else:
                    log("В локальном файле нет курса ILS")
            except Exception as fe:
                log(f"Ошибка при чтении локального файла: {fe}")

        raise RuntimeError("Не удалось получить курс ILS ни из API, ни из файла")
    
# получаем курс
ils_rate = get_ils_rate()
print(f"Текущий курс USD → ILS: {ils_rate} ₪ за 1 USD")

# ввод суммы
try:
    usd_amount = float(input("Введите сумму в USD: "))
    log(f"Пользователь ввел сумму: {usd_amount} USD")
except ValueError:
    log("Пользователь ввел некорректное значение")
    print("Неверный ввод!")
    exit(1)

# конвертация
ils_amount = usd_amount * ils_rate
print(f"{usd_amount} USD = {ils_amount:.2f} ₪")
log(f"Конвертировано: {usd_amount} USD = {ils_amount:.2f} ₪")

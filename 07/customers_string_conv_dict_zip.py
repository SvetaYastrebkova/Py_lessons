# Разбиваем на строки и убираем пустые
lines = customers_string.strip().split("\n")

# Заголовки
headers = lines[0].split(",")

# Создаем пустой словарь
customers_dict = {}

# Проходим по всем строкам с данными
for line in lines[1:]:
    values = line.split(",")
    row_dict = {}
    for h, v in zip(headers, values):
        if h != "ip_address":   # убираем ip из вложенного словаря
            row_dict[h] = v
    ip = values[headers.index("ip_address")]  # ключ верхнего словаря
    customers_dict[ip] = row_dict

# Проверка
from pprint import pprint
pprint(customers_dict)

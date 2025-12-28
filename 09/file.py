print(__file__)

import os

file_path = os.path.join("data", "users.csv")
print(file_path)  # data/users.csv


from pathlib import Path

file_path = Path("data") / "users.csv"
print(file_path)  # data/users.csv


'''
Основные возможности pathlib:

Создание путей

p = Path("/home/user/documents")


Навигация по файлам и папкам

print(p.name)       # имя папки/файла -> documents
print(p.parent)     # родительский каталог -> /home/user
print(p.suffix)     # расширение файла (".txt", ".csv" и т. д.)


Обход файлов

for f in Path("data").iterdir():
    print(f)  # выводит все файлы и папки в "data"


Чтение и запись

p = Path("data/users.csv")

text = p.read_text(encoding="utf-8")  # чтение файла как текста
print(text)

p.write_text("новый текст", encoding="utf-8")  # запись в файл


Проверка существования

p.exists()      # True/False
p.is_file()     # проверка, файл ли это
p.is_dir()      # проверка, папка ли это
'''

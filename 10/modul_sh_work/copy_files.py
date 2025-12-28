import shutil
import pathlib

# Папка, где лежит скрипт
ROOT_FOLDER = pathlib.Path(__file__).parent

# Исходная папка "source" рядом со скриптом
SOURCE_FOLDER = ROOT_FOLDER / "source"
SOURCE_FOLDER.mkdir(exist_ok=True)  # создаем папку, если её нет

# Папка назначения "target"
TARGET_FOLDER = ROOT_FOLDER / "target"
TARGET_FOLDER.mkdir(exist_ok=True)

# Список файлов для копирования: (исходное имя, новое имя)
files = [
    ("data.txt", None),
    ("data1.txt", "copy1.txt")
]

for src_name, dst_name in files:
    src_path = SOURCE_FOLDER / src_name

    # Если файла нет, создаем его с тестовым содержимым
    if not src_path.exists():
        print(f"⚠ Файл {src_name} не найден, создаем тестовый файл")
        with src_path.open("w", encoding="utf-8") as f:
            f.write(f"Тестовое содержимое файла {src_name}\n")

    dst_path = TARGET_FOLDER / (dst_name if dst_name else src_name)
    shutil.copy(src_path, dst_path)
    print(f"✅ Скопирован {src_name} → {dst_path}")

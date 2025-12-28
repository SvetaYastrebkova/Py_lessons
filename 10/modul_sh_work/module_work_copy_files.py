import shutil

import pathlib

#copy files

ROOT_FOLDER = pathlib.Path(__file__).parent
SOURCE_FOLDER = ROOT_FOLDER.joinpath("source")
TARGET_FOLDER = ROOT_FOLDER.joinpath("target")
BACKUP_FOLDER = ROOT_FOLDER.joinpath("backup")

# создаем папки, если их нет

SOURCE_FOLDER.mkdir(exist_ok=True)  
TARGET_FOLDER.mkdir(exist_ok=True)
BACKUP_FOLDER.mkdir(exist_ok=True)

# Копируем файл data.txt в папку target
shutil.copy(SOURCE_FOLDER.joinpath("data.txt"),TARGET_FOLDER) 

# Копируем файл data1.txt в target и переименовываем его в copy1.txt
shutil.copy(
    src=SOURCE_FOLDER.joinpath("data1.txt"),
    dst=TARGET_FOLDER.joinpath("copy1.txt")   
)

shutil.copytree(
    src=ROOT_FOLDER,
    dst=BACKUP_FOLDER
)

print(f"Папка {ROOT_FOLDER} скопирована в {BACKUP_FOLDER}")
'''
# копирует папку целиком
shutil.copytree("my_folder", "backup_folder")

# копируеут метаданные
shutil.copystat 

# перемещает папку целиком

shutil.move("file.txt", "new_folder/file.txt")

# удаляет папку со всем содержимым
shutil.rmtree("backup_folder")  

# zip архив
shutil.make_archive("backup", "zip", "my_folder")

# tar.gz архив
shutil.make_archive("backup", "gztar", "my_folder")

shutil.unpack_archive("backup.zip", "extracted_folder")

'''
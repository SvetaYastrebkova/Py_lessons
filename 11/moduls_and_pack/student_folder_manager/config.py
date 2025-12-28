from pathlib import Path

# Основные настройки
GROUP_SIZE = 10
COMPANY_NAME = "my great company"

ROOT_FOLDER = Path(__file__).parent
DATA_FOLDER = ROOT_FOLDER / "data"
STUDENTS_FILE = DATA_FOLDER / "students.json"
OUTPUT_FOLDER = ROOT_FOLDER / COMPANY_NAME

STUDENTS_FOLDERS = ("classwork", "homework")
STUDENTS_PERSONAL_DATA_FILE = "student_data.txt"

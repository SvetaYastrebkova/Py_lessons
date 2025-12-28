import json
from pathlib import Path

GROUP_SIZE = 10 #определяем размер группы
COMPANY_NAME = "my great company" #название компании
STUDENTS_FILE = Path(__file__).parent / "students.json" # путь к файлу в той же папке, что и скрипт
STUDENTS_FOLDERS = ("classwork","homework") #названия папок которые надо создать в каждой папке студента
STUDENTS_PERSONAL_DATA_FILE = 'student_data.txt' #названия файла который надо создать в каждой папке студента
ROOT_FOLDER = Path(__file__).parent
OUTPUT_FOLDER = ROOT_FOLDER / COMPANY_NAME #папка вывода

# проверяем, существует ли файл
if not STUDENTS_FILE.exists():
    print(f"Файл не найден: {STUDENTS_FILE}")
else:
    print(f"Файл найден: {STUDENTS_FILE}")


# Функция для получения студентов из JSON
def get_students(STUDENTS_FILE: str) -> list[dict]:
    with open(STUDENTS_FILE, encoding="utf-8") as f:
        students = json.load(f)
    return students
students = get_students(STUDENTS_FILE)
#print(students)

# Функция для создания курсов. Название курса.
def create_courses(students: list[dict]) -> dict:
    """
    Разбивает студентов по курсам Возвращает словарь: {course_name: [список студентов]}
    """
    courses = {}
    for student in students:
        course_name = student.get("course", "UnknownCourse")
        if course_name not in courses:
            courses[course_name] = []
        courses[course_name].append(student)
    return courses

courses = create_courses(students)
#print(courses)
def create_groups(students: list[dict], GROUP_SIZE) -> dict:
    # Формируем группы для каждого курса
    for course_name, course_students in courses.items():
        group_counter = 1
        for i in range(0, len(course_students), GROUP_SIZE):
            group_students = course_students[i:i+GROUP_SIZE]
            group_id = f"group-{course_name}-{group_counter}"
            groups[group_id] = {"students": group_students}
            group_counter += 1

    return groups

# Создаём группы
groups = create_groups(students, GROUP_SIZE)

print(groups)
''''
# Функция для создания файла с данными студента
def create_student_data_file(student_folder: Path, student: dict):
    """
    Создаёт файл student_data.txt внутри папки студента
    student_folder: Path — путь к папке студента
    student: dict — данные студента (Имя, Фамилия, Курс, почта)
    """
    student_file = student_folder / "student_data.txt"
    with student_file.open("w", encoding="utf-8") as f:
        f.write(f"first_name: {student['first_name']}\n")
        f.write(f"last_name: {student['last_name']}\n")
        f.write(f"course: {student['course']}\n")
        f.write(f"email: {student['email']}\n")
        
        
# Функция для создания папок студентов через Path.mkdir

def create_student_folders(groups: dict, OUTPUT_FOLDER: Path):
    """
    Создаёт структуру папок:
    output_folder / course_name/ group_id / first_name_last_name
    """
    # Создаём корневую папку, если её нет
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
        #папка курса
    for group_id, group_info in groups.items():
        # Из group_id извлекаем название курса
        # group_id имеет формат: "group-<course>-<номер>"
        parts = group_id.split('-')
        if len(parts) >= 3:
            course_name = parts[1]
        else:
            course_name = "UnknownCourse"
        # Папка курса
        course_folder = OUTPUT_FOLDER / course_name
        course_folder.mkdir(parents=True, exist_ok=True)

    for group_id, group_info in groups.items():
        # Папка группы
        group_folder = OUTPUT_FOLDER / course_name / group_id
        group_folder.mkdir(parents=True, exist_ok=True)

        for student in group_info["students"]:
            # Папка студента
            student_folder_name = f"{student['first_name']}_{student['last_name']}"
            student_folder = group_folder / student_folder_name
            student_folder.mkdir(parents=True, exist_ok=True)
create_student_folders(groups, OUTPUT_FOLDER)
        
# Создаём файл с данными студента через отдельную функцию
# create_student_data_file(student_folder, student)

'''
'''
# Функция для печати информации о группах ===
def print_groups(groups: dict):
    print(f"Создано {len(groups)} групп")
    for group_id, group_info in groups.items():
        print(f"{group_id}: {len(group_info['students'])} студентов")
        for student in group_info["students"]:
            print(f"  - {student['Имя']} {student['Фамилия']}")

# === Основной блок ===
if __name__ == "__main__":
    STUDENTS_FILE = "students.json"  # файл со студентами
    GROUP_SIZE = 3
    OUTPUT_FOLDER = pathlib.Path("groups")

    students = get_students(STUDENTS_FILE)
    groups = create_groups(students, GROUP_SIZE)
    create_student_folders(groups, OUTPUT_FOLDER)
    print_groups(groups)
'''
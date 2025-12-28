from pathlib import Path
from config import STUDENTS_PERSONAL_DATA_FILE

def create_student_data_file(student_folder: Path, student: dict):
    """Создаёт файл student_data.txt внутри папки студента"""
    student_file = student_folder / STUDENTS_PERSONAL_DATA_FILE
    with student_file.open("w", encoding="utf-8") as f:
        f.write(f"first_name: {student['first_name']}\n")
        f.write(f"last_name: {student['last_name']}\n")
        f.write(f"course: {student['course']}\n")
        f.write(f"email: {student['email']}\n")

def create_student_folders(groups: dict, output_folder: Path):
    """Создаёт структуру папок для курсов, групп и студентов"""
    output_folder.mkdir(parents=True, exist_ok=True)

    for group_id, group_info in groups.items():
        parts = group_id.split('-')
        course_name = parts[1] if len(parts) >= 3 else "UnknownCourse"

        # Папка курса
        course_folder = output_folder / course_name
        course_folder.mkdir(parents=True, exist_ok=True)

        # Папка группы
        group_folder = course_folder / group_id
        group_folder.mkdir(parents=True, exist_ok=True)

        # Папки студентов
        for student in group_info["students"]:
            student_folder_name = f"{student['first_name']}_{student['last_name']}"
            student_folder = group_folder / student_folder_name
            student_folder.mkdir(parents=True, exist_ok=True)

            create_student_data_file(student_folder, student)

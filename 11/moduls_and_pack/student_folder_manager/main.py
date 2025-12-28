from config import STUDENTS_FILE, OUTPUT_FOLDER, GROUP_SIZE
from utils.student_ops import get_students, create_courses, create_groups
from utils.file_ops import create_student_folders
from utils.printer import print_groups

def main():
    # Читаем студентов
    students = get_students(STUDENTS_FILE)
    
    # Создаём курсы и группы
    courses = create_courses(students)
    groups = create_groups(courses, GROUP_SIZE)

    # Создаём папки и файлы
    create_student_folders(groups, OUTPUT_FOLDER)

    # Выводим инфо
    print_groups(groups)

if __name__ == "__main__":
    main()

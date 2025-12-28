import json
from pathlib import Path
from config import GROUP_SIZE

def get_students(file_path: Path) -> list[dict]:
    """Читаем студентов из JSON"""
    with file_path.open(encoding="utf-8") as f:
        return json.load(f)

def create_courses(students: list[dict]) -> dict:
    """Разбивает студентов по курсам"""
    courses = {}
    for student in students:
        course_name = student.get("course", "UnknownCourse")
        courses.setdefault(course_name, []).append(student)
    return courses

def create_groups(courses: dict, group_size: int = GROUP_SIZE) -> dict:
    """Разбивает студентов на группы"""
    groups = {}
    for course_name, course_students in courses.items():
        group_counter = 1
        for i in range(0, len(course_students), group_size):
            group_students = course_students[i:i+group_size]
            group_id = f"group-{course_name}-{group_counter}"
            groups[group_id] = {"students": group_students}
            group_counter += 1
    return groups

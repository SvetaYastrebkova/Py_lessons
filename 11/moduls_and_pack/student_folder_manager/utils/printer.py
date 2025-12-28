def print_groups(groups: dict):
    """Печатает информацию о группах"""
    print(f"Создано {len(groups)} групп")
    for group_id, group_info in groups.items():
        print(f"{group_id}: {len(group_info['students'])} студентов")
        for student in group_info["students"]:
            print(f"  - {student['first_name']} {student['last_name']}")

CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name TEXT,
    teacher_name TEXT,
    max_students INTEGER
);

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    email TEXT UNIQUE,
    balance REAL DEFAULT 0.0,
    group_id INTEGER,
    FOREIGN KEY(group_id) REFERENCES groups(id)
);

CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS group_courses (
    group_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY(group_id, course_id),
    FOREIGN KEY(group_id) REFERENCES groups(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
);

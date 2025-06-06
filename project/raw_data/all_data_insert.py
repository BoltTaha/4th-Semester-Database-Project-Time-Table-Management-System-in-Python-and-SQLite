import sqlite3

# Connect to your database
conn = sqlite3.connect("timetable.db")
cur = conn.cursor()

# Enforce foreign key constraints
cur.execute("PRAGMA foreign_keys = ON;")

# -------- Departments --------
departments = [
    ("Computer Science",),
    ("Artificial Intelligence",),
    ("Software Engineering",)
]
cur.executemany("INSERT OR IGNORE INTO Departments (DepartmentName) VALUES (?);", departments)

# -------- Get Department IDs for reference --------
cur.execute("SELECT DepartmentID, DepartmentName FROM Departments;")
dept_dict = {name: id for id, name in cur.fetchall()}

# -------- Sections --------
sections = [
    ("2A", dept_dict["Computer Science"]),
    ("2B", dept_dict["Computer Science"]),
    ("2C", dept_dict["Computer Science"]),
    ("2D", dept_dict["Computer Science"]),
    ("4A", dept_dict["Computer Science"]),
    ("4B", dept_dict["Computer Science"]),
    ("4C", dept_dict["Computer Science"]),
    ("4D", dept_dict["Computer Science"]),
    ("AI-2A", dept_dict["Artificial Intelligence"]),
    ("AI-2B", dept_dict["Artificial Intelligence"]),
    ("AI-4A", dept_dict["Artificial Intelligence"]),
    ("AI-4B", dept_dict["Artificial Intelligence"]),
    ("SE-2A", dept_dict["Software Engineering"]),
    ("SE-2B", dept_dict["Software Engineering"]),
    ("SE-4A", dept_dict["Software Engineering"]),
    ("SE-4B", dept_dict["Software Engineering"]),
]
cur.executemany("INSERT OR IGNORE INTO Sections (SectionName, DepartmentID) VALUES (?, ?);", sections)

# -------- Students --------
students = [
    ("23P-0573", "Haris", 5),
    ("23P-0560", "Abdul Rafy", 5),
    ("23P-0559", "Muhammad Taha", 5),
]
cur.executemany("INSERT OR IGNORE INTO Students (RollNumber, StudentName, SectionID) VALUES (?, ?, ?);", students)

# -------- Courses --------
courses = [
    ("EL1005", "Digital Logic Design - Lab", 1, dept_dict["Computer Science"]),
    ("SL1014", "Expository Writing - Lab", 1, dept_dict["Computer Science"]),
    ("MT1004", "Linear Algebra", 3, dept_dict["Software Engineering"]),
    ("CL1004", "Object Oriented Programming - Lab", 1, dept_dict["Computer Science"]),
    ("EE2003", "Computer Organization and Assembly Language", 3, dept_dict["Software Engineering"]),
    ("MG4011", "Entrepreneurship", 3, dept_dict["Software Engineering"]),
    ("CS2009", "Design and Analysis of Algorithms", 3, dept_dict["Software Engineering"]),
    ("CS2005", "Database Systems", 3, dept_dict["Software Engineering"]),
    ("EE1005", "Digital Logic Design", 3, dept_dict["Software Engineering"]),
    ("CS2001", "Data Structures", 3, dept_dict["Software Engineering"]),
    ("EL2003", "Computer Organization and Assembly Language - Lab", 1, dept_dict["Computer Science"]),
    ("AI2002", "Artificial Intelligence", 3, dept_dict["Software Engineering"]),
    ("CS2006", "Operating Systems", 3, dept_dict["Software Engineering"]),
    ("CS2004", "Fundamentals of Software Engineering", 3, dept_dict["Software Engineering"]),
    ("SE2004", "Software Design and Architecture", 3, dept_dict["Software Engineering"]),
    ("CS1005", "Discrete Structures", 3, dept_dict["Software Engineering"]),
    ("SS1014", "Expository Writing", 3, dept_dict["Software Engineering"]),
    ("MT2005", "Probability and Statistics", 3, dept_dict["Software Engineering"]),
    ("MG2013", "Fundamentals of Accounting", 3, dept_dict["Software Engineering"]),
    ("CS1004", "Object Oriented Programming", 3, dept_dict["Software Engineering"]),
]
cur.executemany("INSERT OR IGNORE INTO Courses (CourseCode, CourseName, CreditHours, DepartmentID) VALUES (?, ?, ?, ?);", courses)

# -------- Teachers (assigned only to existing departments) --------
teachers = [
    ("Waseem Ullah", "waseem.ullah@nu.edu.pk", dept_dict["Computer Science"]),
    ("Abdul Basit Khan", "abdul.basit.khan@nu.edu.pk", dept_dict["Artificial Intelligence"]),
    ("Hafeez Ur Rehman", "hafeez.ur.rehman@nu.edu.pk", dept_dict["Software Engineering"]),
    ("M Saood Sarwar", "m.saood.sarwar@nu.edu.pk", dept_dict["Computer Science"]),
    ("Kashif Javed", "kashif.javed@nu.edu.pk", dept_dict["Computer Science"]),
    ("Rabia Zia", "rabia.zia@nu.edu.pk", dept_dict["Artificial Intelligence"]),
    ("Askar Ali", "askar.ali@nu.edu.pk", dept_dict["Software Engineering"]),
    ("Qasim Jan", "qasim.jan@nu.edu.pk", dept_dict["Computer Science"]),
    ("Noreen Shah", "noreen.shah@nu.edu.pk", dept_dict["Software Engineering"]),
    ("Shoaib M Khan", "shoaib.m.khan@nu.edu.pk", dept_dict["Software Engineering"]),
]
cur.executemany("INSERT OR IGNORE INTO Teachers (TeacherName, Email, DepartmentID) VALUES (?, ?, ?);", teachers)

# -------- Rooms --------
rooms = [
    ("Embedded Systems Lab", "Lab", 40),
    ("CALL Lab", "Lab", 40),
    ("Room 5", "Lecture", 40),
    ("Room 6", "Lecture", 40),
    ("Room 2", "Lecture", 40),
    ("Room 4", "Lecture", 40),
    ("Room 3", "Lecture", 40),
    ("Hassan Abidi/SE/Database Lab", "Lab", 40),
    ("Room 9", "Lecture", 40),
    ("Room 11", "Lecture", 40),
    ("Room 12", "Lecture", 40),
    ("Room 10", "Lecture", 40),
    ("Room 7", "Lecture", 40),
    ("Room 8", "Lecture", 40),
]
cur.executemany("INSERT OR IGNORE INTO Rooms (RoomName, RoomType, Capacity) VALUES (?, ?, ?);", rooms)

# -------- Days --------
days = [
    ("Monday",),
    ("Tuesday",),
    ("Wednesday",),
    ("Thursday",),
    ("Friday",),
    ("Saturday",),
    ("Sunday",)
]
cur.executemany("INSERT OR IGNORE INTO Days (DayName) VALUES (?);", days)

# -------- TimeSlots --------
slots = [
    ("08:00", "09:20", "Slot 1"),
    ("09:20", "10:40", "Slot 2"),
    ("10:40", "12:00", "Slot 3"),
    ("12:00", "13:20", "Slot 4"),
    ("13:20", "14:40", "Slot 5"),
    ("14:40", "16:00", "Slot 6"),
]
cur.executemany("INSERT OR IGNORE INTO TimeSlots (StartTime, EndTime, SlotName) VALUES (?, ?, ?);", slots)

# -------- Teacher Office Rooms --------
office_rooms = [
    (f"Room 10{i}",) for i in range(1, 26)
]
cur.executemany("INSERT OR IGNORE INTO TeacherOfficeRooms (RoomName) VALUES (?);", office_rooms)


conn.commit()
conn.close()

print(" All data inserted safely and correctly.")

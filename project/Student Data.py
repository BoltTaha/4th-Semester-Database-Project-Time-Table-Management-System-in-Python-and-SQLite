import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("timetable.db")
cur = conn.cursor()

# Enable foreign key constraints
cur.execute("PRAGMA foreign_keys = ON;")

# Insert students (linked to SectionID = 5 → 4A CS)
students = [
    ("23P-0573", "Haris", 5),
    ("23P-0560", "Abdul Rafy", 5),
    ("23P-0559", "Muhammad Taha", 5)
]
cur.executemany("""
INSERT OR IGNORE INTO Students (RollNumber, StudentName, SectionID) 
VALUES (?, ?, ?);
""", students)

# Insert missing ClassTypes
class_types = [
    (1, "Lecture"),
    (2, "Lab")
]
cur.executemany("""
INSERT OR IGNORE INTO ClassTypes (ClassTypeID, ClassTypeName)
VALUES (?, ?);
""", class_types)

# Insert Semester if not exists
cur.execute("""
INSERT OR IGNORE INTO Semesters (SemesterID, SemesterName)
VALUES (1, 'Spring 2025');
""")

# Insert Course Offerings (CourseID, TeacherID, SectionID, SemesterID)
course_offerings = [
    (1, 8, 5, 1),  # DB Systems - Qasim Jan
    (2, 1, 5, 1),  # DAA - Waseem
    (3, 3, 5, 1)   # OS - Hafeez
]
cur.executemany("""
INSERT OR IGNORE INTO CourseOfferings (CourseID, TeacherID, SectionID, SemesterID)
VALUES (?, ?, ?, ?);
""", course_offerings)

# Get mapping of CourseID → OfferingID
cur.execute("""
SELECT OfferingID, CourseID 
FROM CourseOfferings 
WHERE SectionID = 5 AND SemesterID = 1
""")
offering_map = {row[1]: row[0] for row in cur.fetchall()}

# Safety check (optional)
for cid in [1, 2, 3]:
    if cid not in offering_map:
        print(f"❌ CourseID {cid} not found in offerings!")

# Insert Class Times (OfferingID, DayID, SlotID, RoomID, ClassTypeID)
class_times = [
    (offering_map[1], 1, 1, 8, 2),  # DB Systems (Lab), Monday Slot 1, DB Lab
    (offering_map[2], 2, 2, 3, 1),  # DAA (Lecture), Tuesday Slot 2, Room 5
    (offering_map[3], 3, 3, 4, 1)   # OS (Lecture), Wednesday Slot 3, Room 6
]
cur.executemany("""
INSERT OR IGNORE INTO ClassTimes (OfferingID, DayID, SlotID, RoomID, ClassTypeID)
VALUES (?, ?, ?, ?, ?);
""", class_times)

# Final commit and close
conn.commit()
conn.close()

print("✅ Students, course offerings, and class times inserted successfully.")

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("timetable.db")
cur = conn.cursor()

# Enforce foreign key constraints
cur.execute("PRAGMA foreign_keys = ON;")

# Insert admin records
admins = [
    ("rafay", "rafay123"),
    ("haris", "haris123"),
    ("taha", "taha123")
]

cur.executemany("INSERT OR IGNORE INTO Admins (Username, Password) VALUES (?, ?);", admins)

# Commit changes and close connection
conn.commit()
conn.close()

print(" Admins inserted successfully.")

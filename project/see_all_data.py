import sqlite3

# Connect to the existing database
conn = sqlite3.connect("timetable.db")
cur = conn.cursor()

#  Enable foreign key constraint (good practice)
cur.execute("PRAGMA foreign_keys = ON;")

#  Get all table names except internal sqlite ones
cur.execute("""
    SELECT name FROM sqlite_master 
    WHERE type='table' AND name NOT LIKE 'sqlite_%';
""")
tables = cur.fetchall()

#  For each table, fetch and print all rows
for table_name in tables:
    table = table_name[0]
    print(f"\n🔹 Table: {table}")
    print("-" * (10 + len(table)))

    try:
        cur.execute(f"SELECT * FROM {table}")
        rows = cur.fetchall()
        columns = [description[0] for description in cur.description]

        # Print column names
        print(" | ".join(columns))
        print("-" * (len(" | ".join(columns))))

        # Print rows
        if rows:
            for row in rows:
                print(" | ".join(str(item) if item is not None else "NULL" for item in row))
        else:
            print("⚠️ No data found.")
    except sqlite3.Error as e:
        print(f"❌ Error reading table {table}: {e}")

#  Close the connection
conn.close()

import sqlite3
from pathlib import Path

DB = Path(__file__).parent / "data.db"

conn = sqlite3.connect(DB)
conn.row_factory = sqlite3.Row  # lets you access columns by name
cur = conn.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id   INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT    NOT NULL,
        age  INTEGER,
        city TEXT
    )
""")

# Insert rows (only if table is empty)
cur.execute("SELECT COUNT(*) FROM users")
if cur.fetchone()[0] == 0:
    cur.executemany(
        "INSERT INTO users (name, age, city) VALUES (?, ?, ?)",
        [("Alice", 30, "Austin"), ("Bob", 25, "Denver"), ("Carol", 35, "Chicago")]
    )
    conn.commit()
    print("Inserted 3 rows.")

# Select all
print("\n=== All users ===")
for row in cur.execute("SELECT * FROM users"):
    print(dict(row))

# Filter query
print("\n=== age > 26 ===")
for row in cur.execute("SELECT name, city FROM users WHERE age > ?", (26,)):
    print(dict(row))

# Update
cur.execute("UPDATE users SET city = ? WHERE name = ?", ("Boston", "Bob"))
conn.commit()

# Verify
print("\n=== After update ===")
for row in cur.execute("SELECT * FROM users"):
    print(dict(row))

conn.close()

# SQLite pros/cons note:
# + Zero setup, single file, full SQL, great for local/embedded apps
# - Single writer at a time; not suited for multi-user/server apps
# - Built into Python stdlib (no install needed)

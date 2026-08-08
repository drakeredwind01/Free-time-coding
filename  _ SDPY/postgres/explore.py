import os
import subprocess
import time
from pathlib import Path

import psycopg2
import psycopg2.extras

HERE      = Path(__file__).parent
DATA_DIR  = HERE / "pgdata"    # cluster lives here
SOCKET    = "/tmp/pg_sdpy"     # unix sockets can't handle spaces in paths
PORT      = 5455               # non-default port, avoids clashing with system postgres
LOG       = HERE / "postgres.log"
DB        = "explore_db"
USER      = os.environ["USER"]


def pg(cmd, **kw):
    return subprocess.run(cmd, check=True, text=True, capture_output=True, **kw)


# ── 1. Init cluster if first run ──────────────────────────────────────────────
os.makedirs(SOCKET, exist_ok=True)

if not DATA_DIR.exists():
    pg(["initdb", "-D", str(DATA_DIR), "--no-instructions"])
    print(f"Initialized cluster at {DATA_DIR}")

# ── 2. Start local server ─────────────────────────────────────────────────────
status = subprocess.run(
    ["pg_ctl", "status", "-D", str(DATA_DIR)],
    capture_output=True, text=True
)
if "no server running" in status.stdout:
    pg(["pg_ctl", "start", "-D", str(DATA_DIR),
        "-l", str(LOG),
        "-o", f"-k {SOCKET} -p {PORT} -h ''"])
    time.sleep(1.5)
    print("PostgreSQL started (local cluster).")

# ── 3. Create database if needed ──────────────────────────────────────────────
existing = subprocess.run(
    ["psql", "-h", SOCKET, "-p", str(PORT), "-U", USER,
     "-lqt", "--no-password"],
    capture_output=True, text=True
)
if DB not in existing.stdout:
    pg(["createdb", "-h", SOCKET, "-p", str(PORT), "-U", USER, DB])
    print(f"Created database '{DB}'.")

# ── 4. Connect & explore ──────────────────────────────────────────────────────
conn = psycopg2.connect(host=SOCKET, port=PORT, dbname=DB, user=USER)
conn.autocommit = True
cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id   SERIAL PRIMARY KEY,
        name TEXT    NOT NULL,
        age  INTEGER,
        city TEXT
    )
""")

cur.execute("SELECT COUNT(*) FROM users")
if cur.fetchone()["count"] == 0:
    cur.executemany(
        "INSERT INTO users (name, age, city) VALUES (%s, %s, %s)",
        [("Alice", 30, "Austin"), ("Bob", 25, "Denver"), ("Carol", 35, "Chicago")]
    )
    print("Inserted 3 rows.")

print("\n=== All users ===")
cur.execute("SELECT * FROM users ORDER BY id")
for row in cur.fetchall():
    print(dict(row))

print("\n=== age > 26 ===")
cur.execute("SELECT name, city FROM users WHERE age > %s", (26,))
for row in cur.fetchall():
    print(dict(row))

cur.execute("UPDATE users SET city = %s WHERE name = %s", ("Boston", "Bob"))

print("\n=== After update ===")
cur.execute("SELECT * FROM users ORDER BY id")
for row in cur.fetchall():
    print(dict(row))

cur.close()
conn.close()

# ── 5. Stop server ────────────────────────────────────────────────────────────
pg(["pg_ctl", "stop", "-D", str(DATA_DIR), "-m", "fast"])
print("\nPostgreSQL stopped.")
print(f"Data lives in: {DATA_DIR}")

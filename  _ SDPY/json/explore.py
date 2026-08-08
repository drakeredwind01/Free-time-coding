import json
from pathlib import Path

HERE = Path(__file__).parent

data = {
    "users": [
        {"id": 1, "name": "Alice", "age": 30, "city": "Austin"},
        {"id": 2, "name": "Bob",   "age": 25, "city": "Denver"},
    ],
    "settings": {
        "debug": True,
        "version": "1.0.0"
    }
}

path = HERE / "data.json"

# Write
path.write_text(json.dumps(data, indent=2))
print("=== Written to data.json ===")
print(path.read_text())

# Read back
loaded = json.loads(path.read_text())
print("=== Loaded back ===")
for user in loaded["users"]:
    print(f"  {user['name']} lives in {user['city']}")

# Simulate a "query" (filter in Python)
print("\n=== Filter: age > 26 ===")
results = [u for u in loaded["users"] if u["age"] > 26]
for u in results:
    print(f"  {u}")

# JSON pros/cons note:
# + Built into Python stdlib, universal format, great for APIs
# - No querying engine; filtering is manual Python code
# - No schema enforcement; easy to write malformed data

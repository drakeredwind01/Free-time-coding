import yaml
from pathlib import Path

HERE = Path(__file__).parent

# Sample data
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

# Write to file
with open(HERE / "data.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)

print("=== Written to data.yaml ===")
with open(HERE / "data.yaml") as f:
    print(f.read())

# Read back
with open(HERE / "data.yaml") as f:
    loaded = yaml.safe_load(f)

print("=== Loaded back ===")
for user in loaded["users"]:
    print(f"  {user['name']} lives in {user['city']}")

# YAML pros/cons note:
# + Human-readable, great for config files
# - Not a database; no querying, indexing, or concurrent writes
# - pip install pyyaml

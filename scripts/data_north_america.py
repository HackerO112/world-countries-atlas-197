import json, os
path = os.path.join(os.path.dirname(__file__), "..", "data", "north_america.json")
with open(path, "r", encoding="utf-8") as f:
    COUNTRIES = json.load(f)

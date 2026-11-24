import json, os
path = os.path.join(os.path.dirname(__file__), "..", "data", "africa.json")
with open(path, "r", encoding="utf-8") as f:
    COUNTRIES = json.load(f)

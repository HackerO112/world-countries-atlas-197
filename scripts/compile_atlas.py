# Master compiler for Atlas 197
import json
import os
import sys

sys.path.insert(0, os.path.abspath("."))
from scripts.model import normalize_country
from scripts.build_readme import generate_readme

CONTINENT_FILES = [
    ("data/africa.json", "Africa", 54),
    ("data/asia.json", "Asia", 49),
    ("data/europe.json", "Europe", 45),
    ("data/north_america.json", "North America", 23),
    ("data/south_america.json", "South America", 12),
    ("data/oceania.json", "Oceania", 14)
]

def compile_all(output_json="countries.json", output_readme="README.md"):
    print("--- Starting Master Atlas Compilation ---")
    all_countries = []
    seen_ids = set()
    missing_files = []

    for path, continent, expected_count in CONTINENT_FILES:
        if not os.path.exists(path):
            missing_files.append((path, continent, expected_count))
            continue
            
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        actual_count = len(data)
        print(f"Loaded {continent}: {actual_count} / {expected_count} countries from {path}")
        if actual_count != expected_count:
            print(f"WARNING: Expected {expected_count} for {continent}, but found {actual_count}!")

        for c in data:
            cid = c.get("id")
            if cid in seen_ids:
                print(f"WARNING: Duplicate country id: {cid}")
            seen_ids.add(cid)
            norm_c = normalize_country(c)
            all_countries.append(norm_c)

    if missing_files:
        print("\nCannot finalize yet. Missing files:")
        for path, cont, exp in missing_files:
            print(f"  - {path} ({cont}, expected {exp})")
        return False

    total = len(all_countries)
    print(f"\nTotal countries aggregated: {total} / 197")
    if total != 197:
        print(f"ERROR: Total count {total} does not match exact required 197!")
        return False

    # Sort all countries by continent then name
    continent_order = {"Africa": 1, "Asia": 2, "Europe": 3, "North America": 4, "South America": 5, "Oceania": 6}
    all_countries.sort(key=lambda c: (continent_order.get(c.get("continent"), 99), c.get("name", "")))

    # Write countries.json
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(all_countries, f, indent=2, ensure_ascii=False)
    print(f"Successfully saved {total} countries to {output_json} ({os.path.getsize(output_json):,} bytes).")

    # Generate README.md
    generate_readme(all_countries, output_readme)
    return True

if __name__ == "__main__":
    success = compile_all()
    if success:
        print("\nMaster compilation finished successfully!")
        sys.exit(0)
    else:
        print("\nCompilation incomplete or failed.")
        sys.exit(1)

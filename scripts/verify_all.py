# Verification script for the World Countries Atlas 197 project
import json
import os
import sys

CANONICAL_COUNTS = {
    "Africa": 54,
    "Asia": 49,
    "Europe": 45,
    "North America": 23,
    "South America": 12,
    "Oceania": 14
}

REQUIRED_ENTITIES = ["Yemen", "Vatican City", "Palestine", "Taiwan", "Kosovo"]

FORBIDDEN_ENTITIES = [
    "Western Sahara", "Abkhazia", "South Ossetia", "Transnistria",
    "Northern Cyprus", "Somaliland", "Nagorno-Karabakh", "Puerto Rico",
    "Greenland", "Hong Kong", "Macau"
]

REQUIRED_KEYS = [
    "id", "name", "officialName", "nativeName", "continent", "subregion", "status",
    "iso2", "iso3", "isoNumeric", "flagEmoji", "flagImage", "mapImage", "landmarkImage",
    "capital", "largestCity", "population2026", "areaKm2", "languages", "currency",
    "government", "callingCode", "timeZone", "drivingSide", "religions", "ethnicGroups",
    "gdpNominal", "gdpPpp", "gdpPerCapita", "shortSummary", "history", "geography",
    "economy", "culture", "landmarks", "sources", "lastUpdated"
]

def verify_dataset(filepath="countries.json"):
    print(f"--- Validating dataset: {filepath} ---")
    if not os.path.exists(filepath):
        print(f"ERROR: {filepath} does not exist!")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    total = len(data)
    print(f"Total entities loaded: {total}")
    if total != 197:
        print(f"FAILURE: Expected exactly 197 entities, found {total}!")
        return False

    # Check continent breakdown
    counts = {}
    names = set()
    errors = []

    for c in data:
        name = c.get("name")
        names.add(name)
        cont = c.get("continent")
        counts[cont] = counts.get(cont, 0) + 1

        # Check required keys
        for k in REQUIRED_KEYS:
            if k not in c:
                errors.append(f"Country '{name}' is missing required key '{k}'")
            elif c[k] is None or c[k] == "":
                errors.append(f"Country '{name}' has empty value for required key '{k}'")

        # Check for placeholders
        for k, v in c.items():
            if isinstance(v, str):
                if "TODO" in v or "PLACEHOLDER" in v:
                    errors.append(f"Country '{name}' field '{k}' contains placeholder: {v[:50]}")

    print("\nContinental Distribution:")
    all_counts_correct = True
    for cont, expected in CANONICAL_COUNTS.items():
        actual = counts.get(cont, 0)
        status = "PASS" if actual == expected else "FAIL"
        if actual != expected:
            all_counts_correct = False
        print(f"  [{status}] {cont}: {actual} / {expected}")

    if not all_counts_correct:
        print("FAILURE: Continent counts mismatch!")
        return False

    # Check required specific entities
    print("\nRequired Specific Entities Check:")
    for req in REQUIRED_ENTITIES:
        if req in names:
            print(f"  [PASS] Present: {req}")
        else:
            print(f"  [FAIL] Missing required entity: {req}")
            errors.append(f"Missing required entity: {req}")

    # Check forbidden separate entries
    print("\nForbidden Separate Entities Check (must not appear as numbered sovereign entries):")
    for forb in FORBIDDEN_ENTITIES:
        if forb in names:
            print(f"  [FAIL] Found forbidden separate entity: {forb}")
            errors.append(f"Forbidden separate entity included: {forb}")
        else:
            print(f"  [PASS] Correctly omitted as separate entity: {forb}")

    if errors:
        print(f"\nFound {len(errors)} validation errors:")
        for e in errors[:10]:
            print(f"  - {e}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more.")
        return False

    print("\nAll dataset validations PASSED perfectly!")
    return True

def verify_files():
    print("\n--- Validating companion project files ---")
    files_ok = True
    
    # 1. index.html
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()
        if "worldCountersAtlas_read_v1" in html and "countries.json" in html and "fetch" in html:
            print("  [PASS] index.html exists and contains valid localStorage key & fetch logic.")
        else:
            print("  [FAIL] index.html missing key components.")
            files_ok = False
    else:
        print("  [FAIL] index.html does not exist.")
        files_ok = False

    # 2. README.md
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.read()
        if "The World Countries Atlas 197" in readme and "GitHub Pages" in readme:
            print(f"  [PASS] README.md exists ({len(readme):,} bytes).")
        else:
            print("  [FAIL] README.md missing key headers.")
            files_ok = False
    else:
        print("  [WAIT] README.md not yet built.")

    return files_ok

if __name__ == "__main__":
    ds_ok = verify_dataset()
    fl_ok = verify_files()
    if ds_ok and fl_ok:
        print("\n🎉 ALL VERIFICATION CHECKS PASSED (197 / 197)!")
        sys.exit(0)
    else:
        print("\n⚠️ Checks pending completion.")
        sys.exit(1)

# Master assembly script for Africa dataset
import json
import os
from scripts.africa_batch1 import COUNTRIES_BATCH1
from scripts.africa_batch2 import COUNTRIES_BATCH2
from scripts.africa_batch3 import COUNTRIES_BATCH3
from scripts.africa_batch4 import COUNTRIES_BATCH4
from scripts.model import normalize_country, JSON_EXPORT_KEYS

CANONICAL_AFRICA_54 = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
    "DR Congo", "Republic of the Congo", "Côte d'Ivoire", "Djibouti", "Egypt",
    "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "The Gambia",
    "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya",
    "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco",
    "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe",
    "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa",
    "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia",
    "Zimbabwe"
]

def main():
    all_countries = []
    all_countries.extend(COUNTRIES_BATCH1)
    all_countries.extend(COUNTRIES_BATCH2)
    all_countries.extend(COUNTRIES_BATCH3)
    all_countries.extend(COUNTRIES_BATCH4)

    print(f"Total collected countries: {len(all_countries)}")
    assert len(all_countries) == 54, f"Expected 54, got {len(all_countries)}"

    # Check names against canonical list
    country_names = [c["name"] for c in all_countries]
    assert country_names == CANONICAL_AFRICA_54, f"Names mismatch!\nExpected: {CANONICAL_AFRICA_54}\nGot: {country_names}"
    print("All 54 country names match canonical list perfectly in exact sequence!")

    # Normalize each country and verify schema
    normalized_list = []
    for i, c in enumerate(all_countries, 1):
        norm = normalize_country(c)
        # Check all required export keys
        for k in JSON_EXPORT_KEYS:
            if k not in norm or norm[k] is None or norm[k] == "":
                raise ValueError(f"Country {norm['name']} has invalid value for key '{k}': {norm.get(k)}")
        
        # Verify specific rich attributes
        assert isinstance(norm["landmarks"], list) and len(norm["landmarks"]) >= 3, f"Too few landmarks in {norm['name']}"
        assert isinstance(norm["majorCities"], list) and len(norm["majorCities"]) >= 3, f"Too few majorCities in {norm['name']}"
        assert "history" in norm and len(norm["history"]) > 100, f"History too short in {norm['name']}"
        assert "recentEvents2020_2026" in norm and len(norm["recentEvents2020_2026"]) > 50, f"Recent events too short in {norm['name']}"
        assert norm["population2026"] > 50000, f"Unusually low population in {norm['name']}"
        assert norm["areaKm2"] > 200, f"Unusually low area in {norm['name']}"
        
        normalized_list.append(norm)

    print("All 54 countries passed normalize_country and strict quality validation checks!")

    # Save to data/africa.json
    output_path = "/home/nothing/Projects/WORLD_INFO/data/africa.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(normalized_list, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(normalized_list)} countries to {output_path}")

    # Verify saved file
    with open(output_path, "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert len(loaded) == 54, f"Expected 54 countries in json, found {len(loaded)}"
    print(f"Verified {output_path} successfully: Exactly 54 countries present.")

    # Write data_africa.py helper
    script_data_path = "/home/nothing/Projects/WORLD_INFO/scripts/data_africa.py"
    with open(script_data_path, "w", encoding="utf-8") as f:
        f.write('import json, os\npath = os.path.join(os.path.dirname(__file__), "..", "data", "africa.json")\nwith open(path, "r", encoding="utf-8") as f:\n    COUNTRIES = json.load(f)\n')
    print(f"Generated helper {script_data_path}")

if __name__ == "__main__":
    main()

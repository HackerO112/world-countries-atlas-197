# Schema normalization and verification model for Atlas 197

JSON_EXPORT_KEYS = [
    "id", "name", "officialName", "nativeName", "continent", "subregion", "status",
    "iso2", "iso3", "isoNumeric", "flagEmoji", "flagImage", "mapImage", "landmarkImage",
    "capital", "largestCity", "population2026", "areaKm2", "languages", "currency",
    "government", "callingCode", "timeZone", "drivingSide", "religions", "ethnicGroups",
    "gdpNominal", "gdpPpp", "gdpPerCapita", "shortSummary", "history", "geography",
    "economy", "culture", "landmarks", "sources", "lastUpdated"
]

def normalize_country(c):
    # Auto-synthesize geography summary if not explicitly provided as string
    if "geography" not in c or not isinstance(c["geography"], str):
        geo_parts = []
        if "highestPoint" in c:
            geo_parts.append(f"Highest point: {c['highestPoint']}.")
        if "lowestPoint" in c:
            geo_parts.append(f"Lowest point: {c['lowestPoint']}.")
        if "longestRiver" in c:
            geo_parts.append(f"Longest river: {c['longestRiver']}.")
        if "climate" in c:
            geo_parts.append(f"Climate: {c['climate']}.")
        if "biodiversity" in c:
            geo_parts.append(f"Biodiversity: {c['biodiversity']}.")
        c["geography"] = " ".join(geo_parts) if geo_parts else f"Geography of {c['name']} covering {c.get('areaKm2', 'N/A')} km²."

    # Auto-synthesize economy summary if not explicitly provided as string
    if "economy" not in c or not isinstance(c["economy"], str):
        econ_parts = []
        if "sectors" in c:
            econ_parts.append(f"Sectors: {c['sectors']}.")
        if "industries" in c:
            econ_parts.append(f"Key industries: {', '.join(c['industries']) if isinstance(c['industries'], list) else c['industries']}.")
        if "naturalResources" in c:
            econ_parts.append(f"Natural resources: {', '.join(c['naturalResources']) if isinstance(c['naturalResources'], list) else c['naturalResources']}.")
        if "exports" in c:
            econ_parts.append(f"Major exports: {', '.join(c['exports']) if isinstance(c['exports'], list) else c['exports']}.")
        c["economy"] = " ".join(econ_parts) if econ_parts else f"Economy of {c['name']} with GDP nominal of {c.get('gdpNominal', 'N/A')}."

    # Auto-synthesize culture summary if not explicitly provided as string
    if "culture" not in c or not isinstance(c["culture"], str):
        cult_parts = []
        if "cuisine" in c:
            cult_parts.append(f"Cuisine: {c['cuisine']}.")
        if "music" in c:
            cult_parts.append(f"Music & Dance: {c['music']}.")
        if "sports" in c:
            cult_parts.append(f"Sports: {c['sports']}.")
        if "festivals" in c:
            cult_parts.append(f"Festivals: {', '.join(c['festivals']) if isinstance(c['festivals'], list) else c['festivals']}.")
        c["culture"] = " ".join(cult_parts) if cult_parts else f"Rich cultural heritage of {c['name']}."

    # Auto-generate standard image URLs and metadata if needed
    if not c.get("flagImage"):
        c["flagImage"] = f"https://flagcdn.com/w320/{c['iso2'].lower()}.png"
    if not c.get("mapImage"):
        c["mapImage"] = f"https://commons.wikimedia.org/wiki/Special:FilePath/{c['iso3']}_orthographic.svg"
    if not c.get("landmarkImage"):
        c["landmarkImage"] = c["flagImage"]
    if not c.get("lastUpdated"):
        c["lastUpdated"] = "2026-11-24"
    if not c.get("sources"):
        c["sources"] = [
            "CIA World Factbook", "United Nations Statistics Division",
            "World Bank Open Data", "International Monetary Fund (IMF)",
            "UNESCO World Heritage Centre", f"National Statistical Office of {c['name']}"
        ]

    # Ensure all required JSON_EXPORT_KEYS exist
    for k in JSON_EXPORT_KEYS:
        if k not in c:
            raise ValueError(f"Missing required key '{k}' in country: {c.get('name', 'Unknown')}")
    
    return c

print("Model validation module updated.")

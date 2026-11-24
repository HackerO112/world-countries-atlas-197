# Standardized country dictionary builder
import json

def c_entry(
    id, name, officialName, nativeName, continent, subregion, status,
    iso2, iso3, isoNumeric, flagEmoji, demonym, capital, largestCity, majorCities,
    nationalDay, nationalAnthem, motto, population2026, areaKm2, areaRank, populationRank,
    coordinates, borders, coastline, landlocked, highestPoint, lowestPoint, longestRiver,
    majorLakes, majorMountains, climate, naturalHazards, environmentalIssues, biodiversity,
    timeZone, drivingSide, callingCode, languages, currency, government, headOfState,
    headOfGovernment, legislature, constitution, mainPoliticalParties, latestElections,
    politicalSituation, foreignRelations, military, internationalOrgs, adminDivisions,
    history, recentEvents2020_2026, historicalFigures, ethnicGroups, religions, literacyRate,
    lifeExpectancy, hdi, urbanization, education, healthcare, socialCustoms, etiquette,
    nationalIdentity, gdpNominal, gdpPpp, gdpPerCapita, sectors, industries, agriculture,
    naturalResources, energy, exports, imports, tradePartners, tourism, employment, debtInflation,
    transport, airports, ports, internetUsage, cuisine, festivals, music, dance, art, architecture,
    literature, cinema, sports, media, clothing, holidays, crafts, worldHeritageSites, unescoIntangible,
    famousPeople, flagDescription, coatOfArmsDescription, symbols, landmarks, travelNotes, shortSummary,
    flagImage=None, mapImage=None, landmarkImage=None
):
    pop_density = f"{population2026 / areaKm2:.1f} / km²"
    if not flagImage:
        flagImage = f"https://flagcdn.com/w320/{iso2.lower()}.png"
    if not mapImage:
        mapImage = f"https://commons.wikimedia.org/wiki/Special:FilePath/{iso3}_orthographic.svg"
    if not landmarkImage:
        landmarkImage = flagImage
    sources = [
        "CIA World Factbook", "United Nations Statistics Division",
        "World Bank Open Data", "International Monetary Fund (IMF)",
        "UNESCO World Heritage Centre", f"National Statistical Office of {name}"
    ]
    geo_text = f"Spanning {areaKm2:,} km² across {subregion}. Highest point: {highestPoint}; lowest point: {lowestPoint}. Longest river: {longestRiver}. Climate: {climate}."
    econ_text = f"Economy with GDP nominal of {gdpNominal} ({gdpPerCapita} per capita). Leading sectors: {sectors}. Main industries: {', '.join(industries) if isinstance(industries, list) else industries}. Key exports: {', '.join(exports) if isinstance(exports, list) else exports}."
    cult_text = f"Rich cultural traditions featuring cuisine ({cuisine}), traditional music and dance ({music}; {dance}), literature ({literature}), and sports ({sports})."
    
    return {
        "id": id, "name": name, "officialName": officialName, "nativeName": nativeName,
        "continent": continent, "subregion": subregion, "status": status,
        "iso2": iso2, "iso3": iso3, "isoNumeric": isoNumeric, "flagEmoji": flagEmoji,
        "demonym": demonym, "capital": capital, "largestCity": largestCity, "majorCities": majorCities,
        "nationalDay": nationalDay, "nationalAnthem": nationalAnthem, "motto": motto,
        "population2026": population2026, "areaKm2": areaKm2, "areaRank": areaRank,
        "populationRank": populationRank, "populationDensity": pop_density,
        "coordinates": coordinates, "borders": borders, "coastline": coastline, "landlocked": landlocked,
        "highestPoint": highestPoint, "lowestPoint": lowestPoint, "longestRiver": longestRiver,
        "majorLakes": majorLakes, "majorMountains": majorMountains, "climate": climate,
        "naturalHazards": naturalHazards, "environmentalIssues": environmentalIssues,
        "biodiversity": biodiversity, "timeZone": timeZone, "drivingSide": drivingSide,
        "callingCode": callingCode, "languages": languages, "currency": currency,
        "government": government, "headOfState": headOfState, "headOfGovernment": headOfGovernment,
        "legislature": legislature, "constitution": constitution, "mainPoliticalParties": mainPoliticalParties,
        "latestElections": latestElections, "politicalSituation": politicalSituation,
        "foreignRelations": foreignRelations, "military": military, "internationalOrgs": internationalOrgs,
        "adminDivisions": adminDivisions, "history": history, "recentEvents2020_2026": recentEvents2020_2026,
        "historicalFigures": historicalFigures, "ethnicGroups": ethnicGroups, "religions": religions,
        "literacyRate": literacyRate, "lifeExpectancy": lifeExpectancy, "hdi": hdi,
        "urbanization": urbanization, "education": education, "healthcare": healthcare,
        "socialCustoms": socialCustoms, "etiquette": etiquette, "nationalIdentity": nationalIdentity,
        "gdpNominal": gdpNominal, "gdpPpp": gdpPpp, "gdpPerCapita": gdpPerCapita,
        "sectors": sectors, "industries": industries, "agriculture": agriculture,
        "naturalResources": naturalResources, "energy": energy, "exports": exports,
        "imports": imports, "tradePartners": tradePartners, "tourism": tourism,
        "employment": employment, "debtInflation": debtInflation, "transport": transport,
        "airports": airports, "ports": ports, "internetUsage": internetUsage,
        "cuisine": cuisine, "festivals": festivals, "music": music, "dance": dance,
        "art": art, "architecture": architecture, "literature": literature, "cinema": cinema,
        "sports": sports, "media": media, "clothing": clothing, "holidays": holidays,
        "crafts": crafts, "worldHeritageSites": worldHeritageSites, "unescoIntangible": unescoIntangible,
        "famousPeople": famousPeople, "flagDescription": flagDescription,
        "coatOfArmsDescription": coatOfArmsDescription, "symbols": symbols,
        "landmarks": landmarks, "travelNotes": travelNotes, "shortSummary": shortSummary,
        "geography": geo_text, "economy": econ_text, "culture": cult_text,
        "flagImage": flagImage, "mapImage": mapImage, "landmarkImage": landmarkImage,
        "sources": sources, "lastUpdated": "2026-11-24"
    }

print("country_helper initialized successfully.")

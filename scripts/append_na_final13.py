import sys, os
sys.path.insert(0, os.path.abspath("."))
import json

from scripts.append_na_final import countries

na_remaining_13 = [
    # 11. Grenada
    {
        "id": "grenada", "name": "Grenada", "officialName": "Grenada", "nativeName": "Grenada",
        "continent": "North America", "subregion": "Caribbean", "status": "UN Member State",
        "iso2": "GD", "iso3": "GRD", "isoNumeric": "308", "flagEmoji": "🇬🇩", "demonym": "Grenadian",
        "capital": "St. George's", "largestCity": "St. George's", "majorCities": ["St. George's", "Gouyave", "Grenville", "Victoria", "Hillsborough (Carriacou)"],
        "nationalDay": "February 7 (Independence Day)", "nationalAnthem": "Hail Grenada", "motto": "Ever Conscious of God We Aspire, Build and Advance as One People",
        "population2026": 126000, "areaKm2": 344, "areaRank": 185, "populationRank": 189, "populationDensity": "366.3 / km²",
        "coordinates": {"lat": 12.1165, "lng": -61.6790}, "borders": [], "coastline": "121 km", "landlocked": False,
        "highestPoint": "Mount Saint Catherine (840 m)", "lowestPoint": "Caribbean Sea (0 m)", "longestRiver": "Great River",
        "majorLakes": ["Grand Etang Lake (volcanic crater lake)"], "majorMountains": ["Mount Saint Catherine"],
        "climate": "Tropical rainy with trade winds; dry season January to May; wet season June to December",
        "naturalHazards": ["Hurricanes (Atlantic hurricane belt)", "Kick 'em Jenny active submarine volcano off north coast"],
        "environmentalIssues": ["Coastal erosion management", "Mangrove wetland conservation in Carriacou"],
        "biodiversity": "The 'Isle of Spice'; lush rainforests, Annandale Falls, nesting leatherback sea turtles at Levera Beach",
        "timeZone": "UTC-04:00", "drivingSide": "left", "callingCode": "+1-473", "languages": ["English", "Grenadian Creole English"],
        "currency": "East Caribbean Dollar (XCD, $)", "government": "Federal parliamentary constitutional monarchy",
        "headOfState": "King Charles III (represented by Governor-General Dame Cécile La Grenade)", "headOfGovernment": "Prime Minister Dickon Mitchell",
        "legislature": "Parliament (Senate and House of Representatives)", "constitution": "1974", "mainPoliticalParties": ["National Democratic Congress (NDC)", "New National Party (NNP)"],
        "latestElections": "General election 2022; general election scheduled 2027",
        "politicalSituation": "Prime Minister Dickon Mitchell guiding sustainable economic transformation, climate diplomacy, and expansion of digital education.",
        "foreignRelations": "Member of CARICOM, OECS, Commonwealth, UN, OAS; champion of small island green and blue economies.",
        "military": "No standing army; Royal Grenada Police Force (RGPF) and Coast Guard.",
        "internationalOrgs": ["UN", "CARICOM", "OECS", "Commonwealth", "OAS", "WTO", "IMF"], "adminDivisions": "6 parishes and 1 dependency (Carriacou and Petite Martinique)",
        "history": "Inhabited by indigenous Caribs (Kalinago). Sighted by Columbus in 1498 (named Concepción). French founded Fort Royal (St. George's) in 1650. Ceded to Britain in 1763; Julien Fédon led major 1795 rebellion against British rule. Gained independence on February 7, 1974 under Sir Eric Gairy. The 1979 New Jewel Movement led by Maurice Bishop established the People's Revolutionary Government until internal crisis led to the 1983 US military intervention (Operation Urgent Fury) and restoration of constitutional democracy.",
        "recentEvents2020_2026": "Celebrated 50th Golden Jubilee of Independence in February 2024; PM Dickon Mitchell assumed chairmanship of CARICOM; expanded marine conservation and organic spice exports.",
        "historicalFigures": ["Maurice Bishop", "Sir Eric Gairy", "Julien Fédon", "Kirani James", "Dame Cécile La Grenade"],
        "ethnicGroups": ["African descent ~82.4%", "Mixed heritage ~13.3%", "East Indian ~2.2%", "Others (European, Indigenous) ~2.1%"],
        "religions": ["Roman Catholic ~44.6%", "Protestant (Anglican ~11.5%, Seventh-day Adventist ~10.5%, Pentecostal ~8.7%) ~44%", "None/Other ~11.4%"],
        "literacyRate": "98.6%", "lifeExpectancy": "75.4 years", "hdi": "0.793 (High)", "urbanization": "36.8%",
        "education": "St. George's University (SGU - world-renowned medical and veterinary school educating thousands of global physicians) and T.A. Marryshow Community College.",
        "healthcare": "General Hospital in St. George's, Princess Alice Hospital in Mirabeau, and Princess Royal Hospital in Carriacou.",
        "socialCustoms": "Spicemas Carnival (Jab Jab masquerade), sharing Oil Down communal feasts, cricket gatherings, storytelling.",
        "etiquette": "Friendly and respectful, polite 'Good morning' greetings, community hospitality.",
        "nationalIdentity": "Celebrated as the 'Isle of Spice' (produces 20% of world nutmeg), home to the world's first underwater sculpture park, and Olympic track greatness.",
        "gdpNominal": "$1.40 billion (approx. 2026)", "gdpPpp": "$2.25 billion (approx. 2026)", "gdpPerCapita": "$11,100",
        "sectors": "Tourism & Education 65%, Agriculture 12%, Construction 15%, Manufacturing 8%", "industries": ["Medical higher education (SGU)", "Tourism and yachting", "Nutmeg and spice processing", "Artisan single-origin organic chocolate (Grenada Chocolate Company)", "Beverages and rum"],
        "agriculture": ["Nutmeg and mace (world's top producer per capita)", "Fine flavor organic cacao", "Cloves, cinnamon, ginger, allspice", "Bananas", "Fresh fish and lobster"],
        "naturalResources": ["Spices and agricultural soils", "Pristine white sand beaches (Grand Anse)", "Marine fisheries", "Geothermal and solar potential"],
        "energy": "Expanding solar installations and geothermal exploration on Mount Saint Catherine",
        "exports": ["Nutmeg and mace", "Fine organic chocolate and cocoa beans", "Fresh fish", "Tropical fruit and vegetables", "Medical education services"],
        "imports": ["Machinery and transport vehicles", "Manufactured goods", "Foodstuffs", "Refined petroleum"],
        "tradePartners": ["United States (largest partner)", "United Kingdom", "Trinidad and Tobago", "Germany", "France"],
        "tourism": "Over 550,000 visitors enjoying Grand Anse Beach (consistently ranked among world's top 10 beaches), Molinere Underwater Sculpture Park, Grand Etang crater lake, and spice plantation tours.",
        "employment": "Medical university operations, tourism hospitality, spice agriculture.", "debtInflation": "XCD pegged 2.70:1 to USD; low and stable inflation.",
        "transport": "Paved scenic coastal roads; Osprey ferry connecting Grenada to Carriacou.",
        "airports": ["Maurice Bishop International Airport (GND at Point Salines)", "Lauriston Airport on Carriacou"],
        "ports": ["Port of St. George's (horseshoe-shaped deepwater harbor / Carenage)"],
        "internetUsage": "82.4%",
        "cuisine": "Oil Down (national one-pot dish: salted meat, chicken, breadfruit, callaloo, and dumplings stewed in rich coconut milk and turmeric until absorbed), Nutmeg ice cream, Fresh grilled fish, Roti, Cocoa tea, Clarke's Court and River Antoine rum.",
        "festivals": ["Spicemas (August Carnival famous for Jab Jab devil masquerade with black molasses and horns)", "Carriacou Maroon and String Band Music Festival", "Grenada Chocolate Festival"],
        "music": "Soca, Calypso, Traditional stringband music of Carriacou, Reggae.",
        "dance": "Jab Jab carnival dance, Big Drum Dance of Carriacou (ancient West African ancestral dance preserved for centuries).",
        "art": "Molinere Underwater Sculpture Park (created by Jason deCaires Taylor - world's first underwater sculpture garden), vibrant Caribbean canvases.",
        "architecture": "Georgian brick and stone colonial buildings with fish-scale tiles in St. George's (often called the prettiest harbor town in the Caribbean); Fort George.",
        "literature": "Merle Collins (Angel, The Colour of Forgetting), Jacob Ross (The Bone Readers).",
        "cinema": "Documentaries on the Grenadian Revolution and world-class marine conservation.",
        "sports": "Athletics (Kirani James - Olympic Gold 2012, Silver 2016, Bronze 2021 in 400m; Lindon Victor - Olympic Bronze 2024 decathlon), Cricket (National Cricket Stadium).",
        "media": "The Grenadian Voice, The New Today, GBN (Grenada Broadcasting Network).",
        "clothing": "National costume in vibrant yellow, red, and green madras; casual island wear.",
        "holidays": ["February 7 (Independence Day)", "Spicemas Carnival Monday and Tuesday (August)", "Thanksgiving Day (October 25)"],
        "crafts": "Nutmeg and spice baskets, woven straw hats, calabash carvings, sea-glass jewelry.",
        "worldHeritageSites": ["Tentative List: Historic District of St. George's, Grenadines Island Group"],
        "unescoIntangible": ["Big Drum Dance of Carriacou and Spicemas Jab Jab traditions"],
        "famousPeople": ["Kirani James", "Maurice Bishop", "Sir Eric Gairy", "Merle Collins", "Dickon Mitchell"],
        "flagDescription": "Rectangular flag with a red border containing six yellow five-pointed stars (top and bottom); central rectangle divided into four triangles (two yellow, two green) bearing a red central disc with a large yellow star, and a stylized nutmeg clove in the hoist triangle.",
        "coatOfArmsDescription": "Supported by an armadillo and a Ramier pigeon, showing Columbus's ship Santa María, topped by seven roses and a golden helmet, with motto 'EVER CONSCIOUS OF GOD WE ASPIRE, BUILD AND ADVANCE AS ONE PEOPLE'.",
        "symbols": {"animal": "Nine-banded armadillo (Tattoo)", "bird": "Grenada dove (critically endangered endemic)", "flower": "Bougainvillea", "tree": "Nutmeg tree"},
        "landmarks": ["Grand Anse Beach", "Molinere Underwater Sculpture Park", "St. George's Harbor (The Carenage)", "Grand Etang National Park & Crater Lake", "Annandale Falls", "River Antoine Rum Distillery (powered by water wheel since 1785)"],
        "travelNotes": "The Isle of Spice; enchanting, safe, aromatic tropical paradise with world-famous diving and beaches.",
        "shortSummary": "Grenada is the captivating 'Isle of Spice' in the southern Caribbean, renowned for producing fragrant nutmeg and fine chocolate, the world's first underwater sculpture park, the pristine sands of Grand Anse, and Olympic track champions.",
        "flagImage": "https://flagcdn.com/w320/gd.png", "mapImage": "https://commons.wikimedia.org/wiki/Special:FilePath/GRD_orthographic.svg",
        "landmarkImage": "https://commons.wikimedia.org/wiki/Special:FilePath/St_Georges_Grenada.jpg",
        "sources": ["CIA World Factbook", "United Nations", "World Bank", "IMF", "UNESCO", "Central Statistical Office of Grenada"], "lastUpdated": "2026-11-24"
    }
]

for c in na_remaining_13:
    countries.append(c)

print(f"Total NA count after Grenada: {len(countries)}")

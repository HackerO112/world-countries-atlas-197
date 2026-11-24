import json

COUNTRIES = []

def add(c):
    COUNTRIES.append(c)

# We load our already prepared first 5 countries from na_raw and initial_3
from scripts.data_north_america import COUNTRIES as initial_3
from scripts.generate_na_all import remaining_20 as initial_2

for c in initial_3:
    add(c)
for c in initial_2:
    add(c)

print(f"Current count: {len(COUNTRIES)}")

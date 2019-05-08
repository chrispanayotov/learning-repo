#Do this same kind of mapping with cities and
#  states/regions in your country or some other country.

vehicular_reg = {
    'Sofia': 'CA',
    'Pernik': 'PK',
    'Plovdiv': 'PB',
    'Varna': 'B',
    'Burgas': 'A',
    'Vidin': 'BH',
    'Shumen': 'H',
    'Blagoevgrad': 'EB',
}

for city, abbrev in list(vehicular_reg.items()):
    print(f"{city} has the abbreviature {abbrev} for vehicles.")

for city, abbrev in list(vehicular_reg.items()):
    print(f"The abbreviature for each city is {city}, {abbrev}.")


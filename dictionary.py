states = {
    "CA": "California",
    "VA": "Virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}

print(states["CA"])
print(states["NV"])

states_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1060000
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3057315
    }
}

print(states_dictionary["NV"]["POPULATION"])
print(states_dictionary["RI"]["NAME"])

states_dictionary2 = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000,
        "CITIES": [
            "FRESNO",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000,
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexander"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000,
        "CITIES": [
            "Bethesda",
            "Baltimore",
            "Annapolis"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1060000,
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 3057315,
        "CITIES": [
            "Carson City"
            "Las Vegas"
            "Reno"
        ]
    }
}
print(states_dictionary2["RI"]["CITIES"][2])


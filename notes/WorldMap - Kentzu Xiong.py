world_map = {
    'Forest': {
        'NAME': "Forest",
        'DESCRIPTION': "You are deep in the forest looking for a path out.",
        'PATHS': {
            'EAST': 'Town',
            'WEST': 'Forest',
            'NORTH': 'Forest',
            'SOUTH': 'Forest'
        }
    },
    'Town': {
        'NAME': "Town",
        'DESCRIPTION': "The name of the town is half broken the other piece gone." 
                       "The entire town is run down and nobody in sight."
                       "There is a house undamaged toward south.",
        'PATHS': {
            'SOUTH': "House",
            'WEST': 'Forest'
        }
    },
    'House': {
        'NAME': "Undamaged House",
        'DESCRIPTION': ""
    },
    'Hallway': {
        'NAME': "Hallway",
        'DESCRIPTION': 'You are in the hallway and all doors locked'
                       'Towards south is the living room.',
        'PATHS': {
            'SOUTH': 'Living room',
            'WEST': 'Bedroom'
        }
    },
    'Living Room': {
        "NAME": 'Living room',
        'DESCRIPTION': 'You are in the Living room and nobody is there.'
                       'To the west is the kitchen and toward the south is the door to outside.',
        'PATHS': {
            'WEST': 'Kitchen',
            'SOUTH': 'Outside',
            'NORTH': 'Hallway'
        }
    },
    'Kitchen': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'You are in the Kitchen.'
                       'There are freshly made food sitting on the stove.',
        'PATHS': {
            'EAST': 'Living room'
        }
    },
    'Outside': {
        'NAME': 'Outside the house',
        'DESCRIPTION': 'You are outside your house but nobody in sight.'
                       "You see your parents car but it's locked."
                       "Towards the east is your parents laboratory and it is not so far.",
        'PATHS': {
            'EAST': 'Laboratory',
            'NORTH': 'Living room'
        }
    },
    'Outside Laboratory': {
        'NAME': 'Laboratory',
        'DESCRIPTION': 'You are at the laboratory.'
                       'There is a broken door that is open toward east.',
        'PATHS': {
            'EAST': 'Inside laboratory',
            'WEST': 'Outside'
        }
    },
    'Inside Laboratory': {
        'NAME': 'Inside Laboratory',
        'DESCRIPTION': 'There are 3 doors'
                       'east lab, north lab, and south lab.',
        'PATHS': {
            'EAST': 'East lab',
            'NORTH': 'North lab',
            'SOUTH': 'South lab',
            'WEST': 'Laboratory'
        }

    },
    'East Room': {
        'NAME': 'East lab',
        'DESCRIPTION': 'There is a blueprint on a table.',
        'PATHS': {
            'WEST': 'Inside laboratory'
        }
    },
    'North Room': {
        'NAME': 'North lab',
        'DESCRIPTION': 'There are tools here maybe I could use them to build something later',
        'PATHS': {
            'SOUTH': 'Inside laboratory'
        }
    },
    'South Room': {
        'NAME': 'South lab',
        'DESCRIPTION': 'There are tables and shelves but it is all empty.'
                       'A tile in the floor looks odd with light coming through.',
        'PATHS': {
            'DOWN': 'Below laboratory',
            'NORTH': 'Inside laboratory'
        }
    },
    'Below South Room': {
        'NAME': 'Below laboratory',
        'DESCRIPTION': 'There are shelves and broken glass everywhere.'
                       'There is a door towards south and north.',
        'PATHS': {
            'UP': 'South Room'
            'SOUTH': ''
        }
    }
}

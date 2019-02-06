world_map = {
    'House': {
        'NAME': "My House",
        'DESCRIPTION': "You are in your house and getting out of bed."
                       "There is a door east of your bed.",
        'PATHS': {
            'EAST': 'Hallway'
        }
    },
    'Hallway': {
        'NAME': "Hallway",
        'DESCRIPTION': 'You are in the hallway and all doors open'
                       'Towards south is the living room.',
        'PATHS': {
            'SOUTH': 'Living room'
        }
    },
    'Living room': {
        "NAME": 'Living room',
        'DESCRIPTION': 'You are in the Living room and nobody is there.'
                       'To the west is the kitchen and toward the south is the door to outside.',
        'PATHS': {
            'WEST': 'Kitchen',
            'SOUTH': 'Outside'
        }
    },
    'Kitchen': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'You are in the Kitchen.'
                       'There are freshly made food sitting on the stove.'
    },
    'Outside': {
        'NAME': 'Outside the house',
        'DESCRIPTION': 'You are outside your house but nobody in sight.'
                       "You see your parents car but it's locked",
        'PATHS': {

        }
    }
}

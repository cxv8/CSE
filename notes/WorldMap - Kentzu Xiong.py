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
        'DESCRIPTION': ' you are in the hallway and nobody in sight.'
                       'Towards south is the living room.',
        'PATHS': {
            'SOUTH': 'Living room'
        }
    },
    'Living room': {
        "NAME": 'Living room',
        'DESCRIPTION': 'You are in the Living room and nobody is there.'
                       'To the west is the kitchen and and south is outside.',
        'PATHS': {
            'WEST': 'Kitchen',
            'SOUTH': 'Outside'
        }
    }
}

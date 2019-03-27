world_map = {
    'Forest': {
        'NAME': "Forest",
        'DESCRIPTION': "You are deep in the forest looking for a path out."
                       "You are blocked by trees all around you but the east.",
        'PATHS': {
            'EAST': 'Town'
        }
    },
    'Town': {
        'NAME': "Town",
        'DESCRIPTION': "The name of the town is half broken the other piece gone." 
                       "The entire town is run down and nobody in sight."
                       "There is a house undamaged toward south and looking east you see a laboratory not so far away.",
        'PATHS': {
            'SOUTH': "House",
            'WEST': 'Forest',
            'EAST': 'Laboratory'
        }
    },
    'House': {
        'NAME': "Damaged House",
        'DESCRIPTION': "The house looks abandon.",
        'PATHS':{
            'SOUTH': 'Living Room',
            'NORTH': 'Town'
        }
    },
    'Living Room': {
        "NAME": 'Living room',
        'DESCRIPTION': 'You are in the living room and nobody is there and there is a card on the ground.'
                       'To the west is the kitchen and toward the south is the door to outside.',
        'PATHS': {
            'WEST': 'Kitchen',
            'NORTH': 'House'
        }
    },
    'Kitchen': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'You are in the Kitchen.'
                       'The place is empty.',
        'PATHS': {
            'EAST': 'Living room',
        }
    },
    'Laboratory': {
        'NAME': 'Laboratory',
        'DESCRIPTION': 'You are at the laboratory.'
                       'The doors are locked.',
        'PATHS': {
            'EAST': 'Inside laboratory',
            'WEST': 'Town'
        }
    },
    'Inside Laboratory': {
        'NAME': 'Inside Laboratory',
        'DESCRIPTION': 'There are 3 doors labeled'
                       'east lab, north lab, and south lab.',
        'PATHS': {
            'EAST': 'East lab',
            'NORTH': 'North lab',
            'SOUTH': 'South lab',
            'WEST': 'Laboratory'
        }

    },
    'East Lab': {
        'NAME': 'East Lab',
        'DESCRIPTION': 'There is a blueprint on a table.',
        'PATHS': {
            'WEST': 'Inside laboratory'
        }
    },
    'North Lab': {
        'NAME': 'North Lab',
        'DESCRIPTION': 'There are tools here maybe I could use them to build something.',
        'PATHS': {
            'SOUTH': 'Inside laboratory'
        }
    },
    'South Lab': {
        'NAME': 'South Lab',
        'DESCRIPTION': 'There are tables and shelves but it is all empty.'
                       'A tile in the floor looks odd with light coming through.',
        'PATHS': {
            'DOWN': 'Underground laboratory',
            'NORTH': 'Inside laboratory'
        }
    },
    'Underground Room': {
        'NAME': 'Underground Lab Room',
        'DESCRIPTION': 'There are shelves and broken glass everywhere.'
                       'There is a long hallway towards south but no way back up.',
        'PATHS': {
            'SOUTH': 'Maze'
        }
    },
    'Maze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are at the start of a Maze.',
        'PATHS': {
            'NORTH': 'Underground Room',
            'SOUTH': 'SMaze',
            'EAST': 'EMaze',
            'WEST': 'WMaze'
        }
    },
    'SMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.',
        'PATHS': {
            'NORTH': 'Maze',
            'EAST': 'SEMaze'
        }
    },
    'SEMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.',
        'PATHS': {
            'WEST': 'SMaze',
            'NORTH': 'SENMaze',
            'SOUTH': 'SESMaze'
        }
    },
    'SENMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.',
        'PATHS': {
            'North': 'EMaze',
            'EAST': 'SENEMaze',
            'South': 'SEMaze'
        }
    },
    'SENEMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You see the exit of the maze toward south.',
        'PATHS': {
            'SOUTH': 'Exit',
            'WEST': 'SENMaze'
        }
    },
    'Classified': {
        
    }
}

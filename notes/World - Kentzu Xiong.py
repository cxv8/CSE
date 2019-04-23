
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
        'DESCRIPTION': "The name of the town is unknown." 
                       "The entire town is almost destroyed and nobody in sight."
                       "There is a house not so damaged toward south"
                       "toward north is a park"
                       "looking east you see a laboratory not so far away.",
        'PATHS': {
            'SOUTH': 'Front Yard',
            'WEST': 'Forest',
            'EAST': 'Laboratory',
            'NORTH': 'Park'
        }
    },
    'Park': {
        'NAME': 'Park',
        'DESCRIPTION': "There is nothing here but one tree left.",
        'PATHS': {
            'SOUTH': 'Town'
        }
    },
    'Front_Yard': {
        'NAME': "Front Yard",
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
            'NORTH': 'Front Yard'
        }
    },
    'Kitchen': {
        'NAME': 'Kitchen',
        'DESCRIPTION': 'You are in the Kitchen.'
                       'This place is empty.', # ADD METAL BOX
        'PATHS': {
            'EAST': 'Living room',
        }
    },
    'Laboratory': {
        'NAME': 'Laboratory',
        'DESCRIPTION': 'You are at the laboratory.' #FIX DOORS
                       'The doors are broken.',
        'PATHS': {
            'EAST': 'Inside laboratory',
            'WEST': 'Town'
        }
    },
    'Inside Laboratory': {
        'NAME': 'Inside Laboratory',
        'DESCRIPTION': 'There are 3 doors labeled'
                       'east lab, north lab, and south lab.'
                       'At a corner are a lot of parts',
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
        'DESCRIPTION': 'You are at the start of a Maze.'
                       'Go south, east, or west.',
        'PATHS': {
            'NORTH': 'Underground Room',
            'SOUTH': 'SMaze',
            'EAST': 'EMaze',
            'WEST': 'WMaze'
        }
    },
    'SMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.'
                       'Go east', #ADD HERE
        'PATHS': {
            'NORTH': 'Maze',
            'EAST': 'SEMaze'
        }
    },
    'SEMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.'
                       'Go west, north, south.',
        'PATHS': {
            'WEST': 'SMaze',
            'NORTH': 'SENMaze',
            'SOUTH': 'SESMaze'
        }
    },
    'SENMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.'
                       'Go north, east, south.',
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
            'SOUTH': 'Cave',
            'WEST': 'SENMaze'
        }
    },
    'Cave': {
        'NAME': 'Exit to Maze',
        'DESCRIPTION': 'There is an open door toward south.',
        'PATHS': {
            'SOUTH': 'Classified Room',
            'NORTH': 'SENEMaze'
        }
    },
    'Classified Room': {
        'NAME': 'Classified Room',
        'DESCRIPTION': 'There are books and folders all over the floor and some on the shelves.'
                       'There is a folder on a table with another key card next to it.'
                       'There is also something strange about this room.',
        'PATHS': {
            'NORTH': 'Cave',
            'EAST': 'Tunnel' #Print what happened
        }
    },
    'Tunnel': {
        'NAME': 'Tunnel',
        'DESCRIPTION': 'There is a path going up south and another going straight north',
        'PATHS': {
            'NORTH': 'Wall',
            'SOUTH': 'Town'
        }
    },
    'Wall': {
        'NAME': 'Wall',
        'DESCRIPTION': 'You reach an end and on a wall reads:\n'
                       'At a place unknown'
                       'with pieces apart '
                       'head north'
                       'under the dirt'
                       'is where you will find this one part',
        'PATHS': {
            'SOUTH': 'Tunnel'
        }
    }
}

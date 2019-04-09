


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """This method moves a character to a new location
        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


current_node = world_map['']  # ADD IN MAP
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

while playing:
    print(current_node["NAME"])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, down=None, up=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.items = []


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
    'Front Yard': {
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
        'DESCRIPTION': 'A riddle.'
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



Forest = Room('Forest', None, None, 'Town', None, None, None)
Town = Room('Town', 'Park', 'Front Yard', 'Laboratory', 'Forest', None, None)
Park = Room('Park', None, 'Town', None, None, None, None)
Front_Yard = Room('Front_Yard', 'Town', 'Living Room', None, None, None, None)
Living_Room = Room('Living Room', 'Front Yard', None, None, 'Kitchen', None, None)
Kitchen = Room('Kitchen', None, None, 'Living Room', None, None, None)
Laboratory = Room('Laboratory', None, None, 'Inside Laboratory', 'Town', None, None)
Inside_Laboratory = Room('Inside Laboratory', 'North Lab', 'South Lab', 'East Lab', 'Laboratory', None, None)
East_Lab = Room('East Lab', None, None, None, 'Inside Laboratory', None, None)
North_Lab = Room('North Lab', None, 'Inside Laboratory', None, None, None, None)
South_Lab = Room('South Lab', 'Inside Laboratory', None, None, None, 'Underground Room', None)
Underground_Room = Room('Underground Lab Room', None, 'Maze', None, None, None, None)
Maze = Room('Maze', 'Underground Room', 'SMaze', 'EMaze', 'WMaze', None, None)
SMaze = Room('Maze', 'Maze', None, 'SEMaze', None, None, None)
SEMaze = Room(' Maze', 'SENMaze', 'SESMaze', None, 'SMaze', None, None)
SENMaze = Room('Maze', 'EMaze', 'SEMaze', 'SENEMaze', None, None, None)
SENEMaze = Room('Maze', None, 'Cave', None, 'SENMaze', None, None)
Cave = Room('Cave', 'SENEMaze', 'Classified Room', None, None, None, None)
Classified_Room = Room('Classified Room', 'Cave', None, 'Tunnel', None, None, None)
Tunnel = Room('Tunnel', 'Wall', 'Town', None, None, None, None)
Wall = Room('Wall', None, Tunnel, None, None, None, None)
Turn = 100


class LockExecption(Exception):
    pass


class ObjectExecption(Exception):
    pass


print("For all the commands that are available type 'help'.")
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
        'DESCRIPTION': 'You are in the living room and nobody is there and there is a keycard on the ground.'
                       'Toward the south is the door to outside.',
        'PATHS': {
            'NORTH': 'Front Yard'
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
        'DESCRIPTION': 'There are 2 doors labeled'
                       'east lab, and south lab.'
                       'At a corner are a lot of parts',
        'PATHS': {
            'EAST': 'East Lab',
            'SOUTH': 'South Lab',
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
                       'Go east or back north',
        'PATHS': {
            'NORTH': 'Maze',
            'EAST': 'SEMaze'
        }
    },
    'SEMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.'
                       'Go back west, north, or south.',
        'PATHS': {
            'WEST': 'SMaze',
            'NORTH': 'SENMaze',
            'SOUTH': 'SESMaze'
        }
    },
    'SENMaze': {
        'NAME': 'Maze',
        'DESCRIPTION': 'You are in the Maze.'
                       'Go north, east, or back south.',
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
        'DESCRIPTION': 'There are books and folders all over the floor and some on the shelf.'
                       'There is a folder on a table with another key card next to it.'
                       'There is also something strange about how the shelf is placed.',
        'PATHS': {
            'NORTH': 'Cave',
            'EAST': 'Tunnel'
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
        'DESCRIPTION': 'There is a riddle inscribed into the wall.'
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


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, down=None, up=None, description="", items=None):
        super(Room, self).__init__()
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.description = description
        self.items = items


class Part1(object):
    def __init__(self, combination):
        self.combination = combination


class Part2(object):
    def __init__(self, combination):
        self.combination = combination


class Part3(object):
    def __init__(self, combination):
        self.combination = combination


class Tile(object):
    def __init__(self, name):
        self.name = name


class Shelf(object):
    def __init__(self, name):
        self.name = name


class KeyCard(object):
    def __init__(self, name):
        self.name = name


class MasterCard(object):
    def __init__(self, name):
        self.name = name


class Player(object):
    def __init__(self, starting_location, pick_up, drop):
        self.current_location = starting_location
        self.inventory = []
        self.pick_up = pick_up
        self.drop = drop

    def move(self, new_location):
        self.current_location = new_location

keycard = KeyCard("keycard")
MasterCard = MasterCard("MasterCard")
shelf = Shelf("shelf")
tile = Tile("tile")
part1 = Part1("part")
part2 = Part2("part")
part3 = Part3("part")

Forest = Room('Forest', None, None, 'Town', None, None, None,
              "You are deep in the forest looking for a path out."
              " You are blocked by trees all around you but the east."
              )
Town = Room('Town', 'Park', 'Front_Yard', 'Laboratory', 'Forest', None, None,
            "The name of the town is unknown."
            " The entire town is almost destroyed and nobody in sight.\n"
            "There is a house not so damaged toward south"
            " toward north is a park"
            " looking east you see a laboratory not so far away."
            )
Park = Room('Park', None, 'Town', None, None, None, None, "There is nothing here but one tree left.", [part2])
Front_Yard = Room('Front Yard', 'Town', 'Living_Room', None, None, None, None, "The house looks abandon. "
                                                                               "Go south to go in the house.")
Living_Room = Room('Living Room', 'Front_Yard', None, None, None, None, None,
                   'You are in the living room '
                   'and there is a keycard on the ground.'
                   ' Toward the south is the door to outside.', [keycard])
Laboratory = Room('Laboratory', None, None, 'Inside_Laboratory', 'Town', None, None,
                  'You are at the laboratory. Go east to enter.')
Inside_Laboratory = Room('Inside Laboratory', None, 'South_Lab', 'East_Lab', 'Laboratory', None, None,
                         'There are 2 doors named'
                         ' east lab, and south lab.'
                         ' At a corner are a lot of parts', [part1]
                         )
East_Lab = Room('East Lab', None, None, None, 'Inside_Laboratory', None, None,
                'There is a unfinished spaceship and a blueprint on a table with a part next to it.', [part3])
South_Lab = Room('South Lab', 'Inside_Laboratory', None, None, None, 'Underground_Room', None,
                 'There are tables and shelves but it is all empty.'
                 'A tile in the floor looks odd with light coming through.', [tile]
                 )
Underground_Room = Room('Underground Lab Room', None, 'Maze', None, None, None, None,
                        'There are shelves and broken glass everywhere.'
                        'There is a long hallway towards south but no way back up.'
                        )
Maze = Room('Maze', 'Underground_Room', 'SMaze', 'EMaze', 'WMaze', None, None,
            'You are at the start of a Maze.'
            'Go south, east, or west.'
            )
SMaze = Room('Maze', 'Maze', None, 'SEMaze', None, None, None,
             'You are in the Maze.'
             'Go east'
             )
SEMaze = Room(' Maze', 'SENMaze', 'SESMaze', None, 'SMaze', None, None,
              'You are in the Maze.'
              'Go west, north, south.'
              )
SENMaze = Room('Maze', 'EMaze', 'SEMaze', 'SENEMaze', None, None, None,
               'You are in the Maze.'
               'Go north, east, south.'
               )
SENEMaze = Room('Maze', None, 'Cave', None, 'SENMaze', None, None,
                'You see the exit of the maze toward south.')
Cave = Room('Cave', 'SENEMaze', 'Classified_Room', None, None, None, None,
            'There is an broken down door with scratch marks on it toward south.')
Classified_Room = Room('Classified_Room', 'Cave', None, 'Tunnel', None, None, None,
                       'There are books and folders all over the floor and some on the shelves.'
                       'There is a folder on a table with another key card next to it.\n'
                       'There is also something strange about how the shelf is placed.', [MasterCard, shelf]
                       )
Tunnel = Room('Tunnel', 'Wall', 'Town', None, None, None, None,
              'There is a path going up south and another going straight north')
Wall = Room('Wall', None, 'Tunnel', None, None, None, None,
            'you reach an end looking at the wall it reads\n'
            'At a place unknown\n'
            'with pieces apart\n'
            'head north\n'
            'under the dirt\n'
            'is where you will find this one part'
            )
player = Player(Forest, pick_up=True, drop=True)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while playing:
    print("Turn left: %d" % Turn)
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif player.current_location == Park and "dig" in command.lower():
        print("You dug up a part.")
        player.inventory.append(part2)
    elif "move " in command.lower():
        move_name = command.lower()[5:]
        move_object = None

        for item in player.current_location.items:
            if item.name == move_name:
                move_object = item

        if move_object is not None:
            player.current_location.remove(move_object)

    elif "take " in command.lower():
        if player.current_location.items is not None:
            item_name = command.lower()[5:]
            item_object = None
            for item in player.current_location.items:
                if item.name == item_name:
                    item_object = item
                elif item.name == Tile:
                    item_object = None
                elif item.name == Shelf:
                    item_object = None
            if item_object is not None:
                player.inventory.append(item_object)
                player.current_location.items.remove(item_object)
                print("You took the " + item_object.name)
        else:
            print("there is nothing here.")

    elif "pick up " in command.lower():
        if player.current_location.items is not None:
            item_name = command.lower()[5:]
            item_object = None
            for item in player.current_location.items:
                if item.name == item_name:
                    item_object = item
                elif item.name == Tile:
                    item_object = None
                elif item.name == Shelf:
                    item_object = None
            if item_object is not None:
                player.inventory.append(item_object)
                player.current_location.items.remove(item_object)
                print("You took the " + item_object.name)
        else:
            print("there is nothing here.")
    elif "drop " in command.lower():
        items_name = command[5:]
        item_object = None

        for items in player.inventory:
            if items.name == items_name:
                item_object = items

        if item_object is not None:
            player.inventory.remove(item_object)
            player.current_location.items.append(item_object)
            print("%s was dropped" % item_object.name)
    elif "inventory" in command.lower():
        if len(player.inventory) == 0:
            print("You have nothing in your inventory.")
        else:
            for item in player.inventory:
                print(item.name + "\n================")
    elif "help" in command.lower():
        print("To move type:\n'north','south','west','east','up','down' or 'n','s','w','e','u','d'.\n============="
              "============================================================================================\n"
              "To pick up an item in your location type:\n"
              "'pick up' or 'take' then the item in your location.\n======================"
              "==========================================================="
              "========================\nTo exit the game type:\n'q','quit', or 'exit'.\n=========================="
              "===============================================================================\nTo look at your"
              " inventory type 'inventory'.\n========================================================================="
              "================================\nTo drop an item type:\n'drop' then the item you "
              "want to drop in your inventory\n========================================================================"
              "=================================\nTo move an object type:\n'move' then the object\n"
              "========================================================================="
              "================================")
    if player.current_location == East_Lab:
        if [part1, part2, part3] in player.inventory:
            print("You have completed finding all the parts to build the spaceship and had escaped successfully.")
            playing = False
    if Turn == 0:
        print("You did not make it in time.")
        playing = False
    elif command.lower() in directions:
        try:
            room_name = getattr(player.current_location, command)
            if player.current_location == South_Lab and command.lower() in ["down", "d"]:
                if tile in player.current_location:
                    raise ObjectExecption
            if player.current_location == Classified_Room and command.lower() in ["east", "e"]:
                if shelf in player.current_location:
                    raise ObjectExecption
            if player.current_location == Laboratory and command.lower() in ["east", "e"]:
                if keycard not in player.inventory:
                    raise LockExecption
            if player.current_location == Inside_Laboratory and command.lower() in ["east", "e"]:
                if MasterCard not in player.inventory:
                    raise LockExecption
            if room_name is None:
                raise AttributeError
            room_object = globals()[room_name]
            player.move(room_object)
            Turn -= 1

        except LockExecption:
            print("A keycard is needed")
        except ObjectExecption:
            print("You are blocked by and an object.")

        except KeyError:
            print("I can't go that way.")
        except AttributeError:
            print("This key does not exist.")
    print()

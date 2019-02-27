class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description="",):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.npc = []


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


# Put them in quotes
R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking Lot', None, "R19A")


# Players
player = Player(R19A)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # command = 'north'
            room_name = getattr(player.current_location, command)
            room_object = globals()[room_name]

            player.move(room_object)
        except KeyError:
            print("I can't go that way.")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")
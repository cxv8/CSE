class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description="", floor=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
class Player(object):
    def __init__(self,starting_location):
        self.health = 100
        self.current_location = starting_location
        self.chest_slot = 4
        self.inventory = []
        self.damage = 10

def move(self, new_location):
    """This method moves a character to a new location

    :param new_location: The variable containing a room object
    """
    self.current_location = new_location

# Option 1
# Add dependent rooms after
R19A = Room("R19A")
parking_lot = Room("The parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2
# Put them in quotes
R19A = Room("R19A", 'parking_lot')
parking_lot = Room("The parking Lot", None, 'R19A')

player = Player(R19A)
playing = True
directions = ['north', 'south', 'west', 'east', 'up', ' down']
# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            # command = north
            room_object_that_we_move_to = getattr(player.current_location, command)

            # needed for option 2

            room_var = globals()[room_object]

            player.move(room_object)
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command Not Recognized")
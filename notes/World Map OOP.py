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


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, damage, name):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Character(object):
    def __init__(self, health, weapon, armor, name):
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
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon))
        target.take_damage(self.weapon.damage)

# Put them in quotes
R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The parking Lot', None, "R19A")

# Items
sword = Weapon("Sword", 15)
sword2 = Weapon("Orc Sword", 5)

# Players
player = Player(R19A)

# Characters
c1 = Character("Orc1", 100, sword, None)
c2 = Character("Orc2", 100, sword2, None)
c1.attack(c2)

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
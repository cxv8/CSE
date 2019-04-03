


my_sword = Sword("Starter sword", "Metal")
my_sword.swing()

my_Fsword = FireSword("Fire Sword", "Flame Ore")
my_Fsword.fireball(3)

my_Lsword = LightningSword("Linghtning Sword", "Lightning Ore")
my_Lsword.lightning(5)

my_Wsword = WaterSword("Water Sword", "Water Ore")
my_Wsword.water(2)

my_Esword = EarthSword("Earth Sword", "Earth Ore")
my_Esword.swing()

my_WIsword = WindSword("Wind Sword", "Earth Ore")
my_WIsword.wind(3)

hp = HealPotion("Health Potion", "Healing Flower", True)
hp.heal()

stamina = StaminaPotion("Stamina Potion", "Stamina Flower", True)
stamina.stamina()

hs = MegaPotion("Mega Potion", "Healing and Stamina Flower", True)
hs.potion()

my_axe = Axe()
my_axe.swing()

my_Faxe = FasterAxe()
my_Faxe.swing()

my_Longsword = LongSword()
my_Longsword.swing()

my_SLongsword = SLongSword()
my_SLongsword.swing()

my_bow = Bow("Starter Bow", "Wood")
my_bow.shot(4)

my_Wbow = WindBow("Wind Bow", "Wind ore")
my_Wbow.shot(3)


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
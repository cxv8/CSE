class Room(object):
    def __init__(self, name, north=None, south=None, east=None, description="", floor=None):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.floor = floor

# Option 1
# Add dependent rooms after
R19A = Room("R19A")
parking_lot = Room("The parking Lot", None, R19A)

R19A.north = parking_lot

# Option 2
# Put them in quotes
R19A = Room("R19A", 'parking_lot')
parking_lot = Room("The parking Lot", None, 'R19A')

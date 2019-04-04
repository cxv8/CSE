class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


Forest = Room('Forest', None, None, 'Town')
Town = Room('Town', 'Park', 'Front Yard', 'Laboratory', 'Forest')
Park = Room('Park', None, 'Town', None, None)
Front_Yard = Room('Front_Yard', 'Town', 'Living Room', None, None)
Living_Room = Room('Living Room', 'Front Yard', None, None, 'Kitchen')
Kitchen = Room('Kitchen', None, None, 'Living Room', None)
Laboratory = Room('Laboratory', None, None, 'Inside Laboratory', 'Town')
Inside_Laboratory = Room('Inside Laboratory', 'North Lab', 'South Lab', 'East Lab', 'Laboratory')
East_Lab = Room('East Lab', None, None, None, 'Inside Laboratory')
North_Lab = Room('North Lab', None, 'Inside Laboratory', None, None)
South_Lab = Room('South Lab', 'Inside Laboratory', None, None, None)

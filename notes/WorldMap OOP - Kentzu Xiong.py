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


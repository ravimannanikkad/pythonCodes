# A class created for Robot
class Robot:
    #Constructor with attributes name, color and weight
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    # A function to self introduce
    def introduce_self(self):
        print("My name is " + self.name)

# A class created for specifically RaviRobot
# which inherits the Robot class
class RaviRobot(Robot):
    # Constructor with attribute name
    def __init__(self, location):
        self.location = location
    # A function to return the value of location
    def location_now(self):
        print("My name is " + self.name + " and I live in " + self.location)

#****************************************************#
# Created By: Ravi Damodaran
# Organization: Vaayoo
# Classes and Inheritance
#****************************************************#

# Import the classes from the file robot.py
from robot import Robot,RaviRobot

# create object for 1st Robot
r1 = Robot("Ravi","Red",30)
# create object for 2nd Robot
r2 = Robot("Amrita","Yellow",60)
# create object for 3rd Robot using class RaviRobot
r3 = RaviRobot("India")
# Set the inheriting parameters of the class
# RaviRobot using the following
r3.name="Appy"
r3.color="June"
r3.weight=90

#Call the functions in Robot class
r1.introduce_self()
r2.introduce_self()
#Call the functions in RaviRobot class
r3.introduce_self()
r3.location_now()

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Jackson Bailey
#               Colby Clayton
#               Chris Debetta
#               Charlie Robertson
# Section:      562
# Assignment:   Final Project
# Date:         06 12 2022

import turtle

class TurtleSetup:

    START_X = 0
    START_Y = 0
    turtle.setpos(START_X, START_Y)

    def __init__(self, speed: int = 1, pensize: int = 5, color: str = 'blue') -> None:
        """
        Create the setup values for turtle and allow them to be changed

        :param speed: speed of turtle
        :type speed: int
        :param pensize: size of turtle pen
        :type pensize: int
        :param color: color of turtle pen
        :type color: str
        :rtype: None
        """
        self.speed = speed
        turtle.speed(self.speed)
        self.pensize = pensize
        turtle.pensize(pensize)
        self.color = color
        turtle.color(self.color)

    def change_speed(self, speed: int) -> None:
        """
        change the speed of turtle

        :param speed: speed of turtle
        :type speed: int
        :rtype: None
        """
        self.speed = speed
        turtle.speed(self.speed)

    def change_pensize(self, pensize: int) -> None:
        """
        change the pensize of turtle

        :param pensize: size of turtle pen
        :type pensize: int
        :rtype: None
        """
        self.pensize = pensize
        turtle.pensize(self.pensize)

    def change_color(self, color: str) -> None:
        """
        change the color of turtle pen

        :param color: color of turtle pen
        :type color: str
        :rtype: None
        """
        self.color = color
        turtle.color(self.color)


setup = TurtleSetup()


def north(dist):
    """
    Change turtle's heading to north and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(90)
    turtle.forward(dist)


def northeast(dist):
    """
    Change turtle's heading to northeast and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(45)
    turtle.forward(dist)


def northwest(dist):
    """
    Change turtle's heading to north and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(135)
    turtle.forward(dist)


def east(dist):
    """
    Change turtle's heading to east and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(0)
    turtle.forward(dist)


def west(dist):
    """
    Change turtle's heading to west and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(180)
    turtle.forward(dist)


def south(dist):
    """
    Change turtle's heading to south and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(270)
    turtle.forward(dist)


def southeast(dist):
    """
    Change turtle's heading to southeast and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(320)
    turtle.forward(dist)


def southwest(dist):
    """
    Change turtle's heading to southwest and move that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.setheading(225)
    turtle.forward(dist)


def right(dist):
    """
    Turn turtle right and go that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.right(90)
    turtle.forward(dist)


def left(dist):
    """
    Turn turtle left and go that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.left(90)
    turtle.forward(dist)


def slight_right(dist):
    """
    Turn turtle slightly right and go that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.right(45)
    turtle.forward(dist)


def slight_left(dist):
    """
    Turn turtle slightly left and go that direction a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.left(45)
    turtle.forward(dist)


def continue_move(dist):
    """
    Continue moving turtle forward a specified distance

    :param dist: distance in feet
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.forward(dist)

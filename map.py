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

START_X = 0
START_Y = -300
turtle.setpos(START_X, START_Y)


def north(dist: float) -> None:
    """
    Change turtle's heading to north and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(90)
    turtle.forward(dist)


def northeast(dist: float) -> None:
    """
    Change turtle's heading to northeast and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(45)
    turtle.forward(dist)


def north(dist: float) -> None:
    """
    Change turtle's heading to north and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(135)
    turtle.forward(dist)


def east(dist: float) -> None:
    """
    Change turtle's heading to east and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(0)
    turtle.forward(dist)


def west(dist: float) -> None:
    """
    Change turtle's heading to west and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(180)
    turtle.forward(dist)


def south(dist: float) -> None:
    """
    Change turtle's heading to south and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(270)
    turtle.forward(dist)


def southeast(dist: float) -> None:
    """
    Change turtle's heading to southeast and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle movement
    :rtype: None
    """
    turtle.heading(320)
    turtle.forward(dist)


def southwest(dist:float) -> None:
    """
    Change turtle's heading to southwest and move that direction a specified distance

    :param dist: distance in miles
    :type dist: float
    :return: Turtle Movement
    :rtype: None
    """
    turtle.heading(225)
    turtle.forward(dist)

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
    turtle.title('Self Driving Simulation')
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
        turtle.hideturtle()

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
keywordDict = {'north': 90, 'south': 270, 'east': 0, 'west': 180, 'northeast': 45, 'southeast': 320, 'northwest': 135,
               'southwest': 225}
DIST_SCALE = 225


def convert_dir_to_turtle(keywords: list) -> None:
    """
    Convert direction information to turtle headings

    Converts cardinal direction information into turtle headings and moves turtle forward
    :param keywords: route directions
    :type keywords: list
    :rtype: None
    """
    if len(keywords) == 3:
        if keywords[1] + keywords[2] == 'turnright':
            turtle.right(90)
        elif keywords[1] + keywords[2] == 'turnleft':
            turtle.left(90)
        elif keywords[1] + keywords[2] == 'slightright':
            turtle.right(45)
        elif keywords[1] + keywords[2] == 'slightleft':
            turtle.left(45)
    else:
        turtle.setheading(keywordDict[keywords[-1]])


def convert_dist_to_turtle(dist: float) -> None:
    """
    Convert distance information into Turtle distance and scale it to fit

    :param dist: direction distance
    :type dist: float
    :rtype: None
    """
    turtle.forward(dist[-1] // DIST_SCALE)

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
"""
Plot the route using turtle and given directions
"""
import turtle


class TurtleSetup:
    START_X = 0
    START_Y = 0
    turtle.setpos(START_X, START_Y)

    def __init__(self, speed: int = 1, pensize: int = 5, color: str = 'blue', screen_x: int = 1000,
                 screen_y: int = 1000) -> None:
        """
        Create the setup values for turtle and allow them to be changed
        -Jackson Bailey

        :param speed: speed of turtle (default: 1)
        :type speed: int
        :param pensize: size of turtle pen (default: 5)
        :type pensize: int
        :param color: color of turtle pen (default: blue)
        :type color: str
        :param screen_x: x width of the screen (default: 1000)
        :type screen_x: int
        :param screen_y: y height of the screen (default: 1000)
        :type screen_y: int
        :rtype: None
        """
        self.speed = speed
        turtle.speed(self.speed)
        self.pensize = pensize
        turtle.pensize(pensize)
        self.color = color
        turtle.color(self.color)
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.change_screen_size(screen_x, screen_y)

    def change_speed(self, speed: int) -> None:
        """
        change the speed of turtle
        -Jackson Bailey

        :param speed: speed of turtle
        :type speed: int
        :rtype: None
        """
        self.speed = speed
        turtle.speed(self.speed)

    def change_pensize(self, pensize: int) -> None:
        """
        change the pensize of turtle
        -Jackson Bailey

        :param pensize: size of turtle pen
        :type pensize: int
        :rtype: None
        """
        self.pensize = pensize
        turtle.pensize(self.pensize)

    def change_color(self, color: str) -> None:
        """
        change the color of turtle pen
        -Jackson Bailey

        :param color: color of turtle pen
        :type color: str
        :rtype: None
        """
        self.color = color
        turtle.color(self.color)

    def change_screen_size(self, x_width: int, y_width: int) -> None:
        """
        change the window size of turtle screen
        -Chris DeBetta

        :param x_width: x width of screen
        :type x_width: int
        :param y_width: y width of screen
        :type y_width: int
        :rtype: None
        """
        self.screen_x = x_width
        self.screen_y = y_width
        turtle.screensize(x_width, y_width)


setup = TurtleSetup()
keywordDict = {'north': 90, 'south': 270, 'east': 0, 'west': 180, 'northeast': 45, 'southeast': 320, 'northwest': 135,
               'southwest': 225}
DIST_SCALE = 70


def convert_dir_to_turtle(keywords):
    """
        convert keyword values for direction into turtle language and execute
        -Chris DeBetta & Jackson Bailey

        :param keywords: list of direction keywords
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


def convert_dist_to_turtle(dist):
    """
    convert keyword values for distance into turtle language and execute
    -Chris DeBetta & Jackson Bailey

    :param dist: distance forward for turtle
    :type dist: int
    :rtype: None
    """
    turtle.forward(dist[-1] // DIST_SCALE)

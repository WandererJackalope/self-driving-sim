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
Parse directions file into usable format and mess with the file
"""


def convert_mi_ft(dist: float) -> float:
    """
    Convert distance in miles to feet
    -Chris DeBetta

    :param dist: miles
    :type dist: float
    :return: feet
    :rtype: float
    """
    return float(dist) * 5280


def convert_ft_mi(dist: float) -> float:
    """
    convert distance in feet to miles
    -Jackson Bailey

    :param dist: feet
    :type dist: float
    :return: miles
    :rtype: float
    """
    return float(dist) / 5280


class Directions:
    DIR_KEYWORDS = ['north', 'south', 'east', 'west', 'northeast', 'southeast',
                    'northwest', 'southwest', 'left', 'right']
    DIST_KEYWORDS = ['mi', 'ft']
    directions = []
    keyword_directions = []

    def __init__(self, file_name: str) -> None:
        """
        Reads a file and finds the directions and distance in the given file.
        Looks for the cardinal directions in a file along for keywords such as turn left/right.
        Finds the distance and if in feet converts it to feet as it deals in miles.
        -Chris DeBetta

        :param file_name: file with directions and distance
        :type file_name: str
        :rtype: None
        """
        with open(file_name) as myFile:
            self.directions = myFile.read().replace('(', '').replace(')', '').lower().split('\n\n')
            self.directions = [d.split('\n') for d in self.directions]
            # print(self.directions)
            self.find_directions()

    def find_directions(self) -> None:
        """
        Get the direction and distance and add an identifier
        -Chris DeBetta

        :rtype: None
        """
        for i in range(len(self.directions)):
            for j in range(len(self.directions[i])):
                words = self.directions[i][j].split()
                for k in range(len(words)):
                    if words[k] in self.DIR_KEYWORDS:
                        if words[k - 1] in ['slight', 'turn']:
                            self.keyword_directions.append(['DIR', words[k - 1], words[k]])
                        elif words[k] not in ['left', 'right']:
                            self.keyword_directions.append(['DIR', words[k]])
                    elif words[k] in self.DIST_KEYWORDS:
                        if words[k] == 'mi':
                            self.keyword_directions.append(['DIST', convert_mi_ft(float(words[k - 1]))])
                        else:
                            self.keyword_directions.append(['DIST', float(words[k - 1])])

    def get_directions(self) -> list:
        """
        Get raw directions from the file

        :return: list of raw directions
        :rtype: list
        """
        return self.directions

    def get_kwd_directions(self):
        """
        Get stripped directions from the file

        :return: stripped directions
        :rtype: List[List[str]]
        """
        return self.keyword_directions

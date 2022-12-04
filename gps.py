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
# Date:         04 12 2022

def convert_mi_ft(dist):
    return float(dist) * 5280


class GPS:
    DIR_KEYWORDS = ['north', 'south', 'east', 'west', 'northeast', 'southeast', 'northwest', 'southwest', 'left',
                    'right', 'continue']
    DIST_KEYWORDS = ['mi, ft']
    START_X = 0
    START_Y = -300
    directions = []
    keywordDirections = []

    def __init__(self, file_name):
        with open(file_name) as myFile:
            self.directions = myFile.read().lower().split('\n\n')
            self.directions = [d.split('\n') for d in self.directions]
        self.translate_directions()

    def translate_directions(self):
        for x in range(len(self.directions)):
            for y in range(len(self.directions[x])):
                words = self.directions[x][y].split()
                for z in range(len(words)):
                    if words[z] in self.DIR_KEYWORDS:
                        self.keywordDirections.append(['DIR', words[z]])
                    elif words[z] in self.DIST_KEYWORDS:
                        if words[z] == 'mi':
                            self.keywordDirections.append(['DIST', convert_mi_ft(words[z - 1])])
                        else:
                            self.keywordDirections.append(['DIST', int(words[z - 1])])

    def get_directions(self):
        return self.directions

    def get_kwd_directions(self):
        return self.keywordDirections

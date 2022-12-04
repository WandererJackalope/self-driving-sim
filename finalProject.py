class GPS:
    # define constants
    DIR_KEYWORDS = 'north south east west northeast southeast northwest southwest left right continue'.split()
    DIST_KEYWORDS = 'mi ft'.split()
    STARTX = 0
    STARTY = -300

    # define instance variables, not necessary but good for visualization
    directions = []
    keywordDirections = []

    def __init__(self, fileName):  # constructor
        with open(fileName) as myFile:
            # split directions into a nested list
            self.directions = myFile.read().lower().split('\n\n')
            self.directions = [d.split('\n') for d in self.directions]
        self.translateDirections()  # call function to initialize other list, done for readability

    def translateDirections(self):
        for x in range(len(self.directions)):
            for y in range(len(self.directions[x])):
                words = self.directions[x][y].split()  # split each string by space to get each individual word
                for z in range(len(words)):
                    if (words[z] in self.DIR_KEYWORDS):  # if word is used for direction, append to list w/ keyword
                        self.keywordDirections.append(['DIR', words[z]])
                    elif (words[z] in self.DIST_KEYWORDS):  # if word is used for distance, append to list w/ keyword
                        if (words[z] == 'mi'):  # if dist is in miles, convert to feet for standardized unit
                            self.keywordDirections.append(['DIST', self.convertDist(words[z - 1])])
                        else:
                            self.keywordDirections.append(['DIST', int(words[z - 1])])

    def convertDist(self, dist):  # used to convert all distances to feet
        return int(float(dist) * 5280)

    def getDirections(self):  # get method
        return self.directions

    def getKWDirections(self):  # get method
        return self.keywordDirections


gps = GPS('Kyle2VetPk.txt')
print(gps.getKWDirections())

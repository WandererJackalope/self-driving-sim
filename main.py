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
import gps
import map

# file_name = input('Please enter the name of the file to map: ')
directions = gps.Directions('Easterwood2Coulter.txt').get_kwd_directions()
print(directions)
for direction in directions:
    if direction[0] == 'DIR':
        map.convert_dir_to_turtle(direction)
    else:
        map.convert_dist_to_turtle(direction)
turtle.done()

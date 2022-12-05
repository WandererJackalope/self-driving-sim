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

import gps
import map

# file_name = input('Please enter the name of the file to map: ')
directions = gps.Directions('Easterwood2Coulter.txt').get_kwd_directions()
for step in range(0, len(directions), 2):
    # map the route with turtle
    distance: float = float(directions[step + 1][1])
    distance = distance / 65
    move_dir: str = directions[step][2]
    turn_modifier: str = directions[step][1]
    if move_dir == 'north':
        map.north(distance)
    elif move_dir == 'northeast':
        map.northeast(distance)
    elif move_dir == 'northwest':
        map.northwest(distance)
    elif move_dir == 'east':
        map.east(distance)
    elif move_dir == 'west':
        map.west(distance)
    elif move_dir == 'south':
        map.south(distance)
    elif move_dir == 'southeast':
        map.southeast(distance)
    elif move_dir == 'southwest':
        map.southwest(distance)
    elif turn_modifier + ' ' + move_dir == 'turn right':
        map.right(distance)
    elif turn_modifier + ' ' + move_dir == 'turn left':
        map.left(distance)
    elif turn_modifier + ' ' + move_dir == 'slight right':
        map.slight_right(distance)
    elif turn_modifier + ' ' + move_dir == 'slight left':
        map.slight_left(distance)
    elif move_dir == 'continue':
        map.continue_move(distance)

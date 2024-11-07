#File: Origami.py
'''
Mathish origami

angles: Describes all creases coming from a single point. A 2d array with two rows and any amount of columns. Each column describes a fold, the second row will describe the value of mountain: 1 or valley: -1 fold. The first row describes the angle in degrees it has between the reference point of positive right line in a counter clockwise direction. The centerpoint of a waterbomb base can be described as [[-1, 1, 1, -1, 1, 1], [0, 45, 135, 180, 225, 315]]

vertcies: decribes all verticies of a certain polygon when refering to polygon packing. Decribes a set of verticies on a 2d grid, includes their x and y position as in verticies = np.array([[x1, x2, x3], [y1, y2, y3]]) as each vertex is (x1, y1)...
'''

import numpy as np

def flat_foldable(angles):
    #Determines if an angle is flat foldable based on Kawasaki's Theorem and a difference of mountain and valleys being +-2
    total_difference = 0
    for x in range(len(angles[0])):
        total_difference += angles[1][x]
    if np.absolute(total_difference) != 2:
        print('mismatched number of folds')
        return False
        
    total = angles[0][0]
    for x in range(0, len(angles[0]) - 1):
        if (x % 2) == 0:
            total -= (angles[0][x + 1] - angles[0][x])
        else:
            total += (angles[0][x + 1] - angles[0][x])
    if len(angles[0]) % 2 == 0:
        total += 360 - angles[0][len(angles[0]) - 1]
    else:
        total -= 360 - angles[0][len(angles[0]) - 1]
    if (total == 0):
        return True
    return False

def find_center_vertex(verticies):
    #finds the center vertex of a polygon, useful for collapsing and precreasing
    return np.array([(np.sum(verticies[0])/len(verticies[0])), (np.sum(verticies[1])/len(verticies[1]))])

def angle_bisect(angles, angle_1, angle_2, type):
    #will add a bisected angle into the 2darray, bisects in angles between angle 1 and angle 2 with type specified as a integer
    angle = (angles[0][angle_2] + angles[0][angle_1]) / 2
    for x in range(len(angles[0])):
        if angle > angles[0][x]:
            i = x + 1
    return np.array([np.insert(angles[0], i, angle), np.insert(angles[1], i, type)])
    
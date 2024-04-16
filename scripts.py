import math
import numpy as np
O = 0.7
C = 0.78
H = 0.35
N = 0.71            #these are the covalent radii of the atoms

def connection_checker(first_line, second_line):



    first_x = float(first_line[1])
    first_y = float(first_line[2])
    first_z = float(first_line[3])


    second_x = float(second_line[1])
    second_y = float(second_line[2])
    second_z = float(second_line[3])
    d = math.sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2 + (first_z - second_z) ** 2)
    if d > 3:
        return ["1", d]
    return ["0", d]


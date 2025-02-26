import math
import timeit
import random

def collinearPoints(points):
    result = []
    for point in points:
        slopes = []
        for other in points:
            if other != point:
                if other[0] - point[0] == 0:
                    slope = float('int')
                else:
                    slope = (other[1]-point[0])/(other[1]-point[0])
                slopes.append((slope,other))
            slopes.sort(key=lambda x:(x[0],x[1][0],x[1][1]))
        result.append(slopes)
    return result

input = [(0,0), (1,1), (3,3), (4,4), (6,6), (7,7), (9,9)]
result = collinearPoints(input)

for element in result:
    print(element)

# input = [(1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (8,0)]
# collinearPoints(input)

# input = [(7,0), (14,0), (22,0), (27,0), (31,0), (42,0)]
# collinearPoints(input)

# input = [(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,-2), (0,-53)]
# collinearPoints(input)

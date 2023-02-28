import math
import random

# Fungsi randomize point


def randomPoint(n, d):
    point = []
    for i in range(n):
        temp = []
        for i in range(d):
            temp.append(round(random.uniform(-100, 100), 2))
        point.append(temp)
    return point

# Function menghitung euclidean distance


def euclidDistance(point1, point2, countEuclid):
    countEuclid += 1
    # print(countEuclid)
    dis = 0
    for i in range(0, len(point1)):
        temp = point2[i] - point1[i]
        dis += math.pow(temp, 2)

    return math.sqrt(dis), countEuclid

# Formatting output point


def printPoint(point):
    print("(", end='')
    for i in range(len(point)):
        print(point[i], end='')
        if (i == len(point) - 1):
            print(")")
        else:
            print(", ", end='')

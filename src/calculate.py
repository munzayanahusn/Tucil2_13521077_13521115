import math
import numpy

# Perhitungan jarak


def euclidDistance(point):
    dis = 0
    for i in range(len(point)):
        temp = point[i][0]
        for j in range(1, len(point[i])):
            temp -= point[i][j]
        dis += math.pow(temp, 2)

    return math.sqrt(dis)

# Proses Divide


def findPair(point):
    # Proses Divide
    if (len(point) <= 2):
        dis = euclidDistance(point[0], point[1])

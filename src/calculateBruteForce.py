import math
from tools import *


def findPairBF(listPoint, countEuclid):
    minDistance, countEuclid = euclidDistance(
        listPoint[0], listPoint[1], countEuclid)
    minPoin1 = listPoint[0]
    minPoin2 = listPoint[1]
    for i in range(len(listPoint)-1):
        for j in range(i+1, len(listPoint)):
            dis, countEuclid = euclidDistance(
                listPoint[i], listPoint[j], countEuclid)
            if (minDistance > dis):
                minDistance = dis
                minPoin1 = listPoint[i]
                minPoin2 = listPoint[j]

    return minDistance, minPoin1, minPoin2, countEuclid

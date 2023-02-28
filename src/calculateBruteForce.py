import math
from tools import *


def findPairBF(listPoint, countEuclid):
    minDistance, countEuclid = euclidDistance(
        listPoint[0], listPoint[1], countEuclid)
    minPoin1 = [listPoint[0]]
    minPoin2 = [listPoint[1]]
    print("\n===========")
    print(len(listPoint))
    for i in range(len(listPoint)):
        print(i)
        for j in range(i+1, len(listPoint)):
            dis, countEuclid = euclidDistance(
                listPoint[i], listPoint[j], countEuclid)
            if (minDistance == dis):
                minPoin1.append(listPoint[i])
                minPoin2.append(listPoint[j])
            elif (minDistance > dis):
                minDistance = dis
                minPoin1 = [listPoint[i]]
                minPoin2 = [listPoint[j]]
            # minDistance < dis
        print("===========\n")

    return minDistance, minPoin1, minPoin2, countEuclid

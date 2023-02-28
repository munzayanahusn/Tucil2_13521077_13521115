import math
from tools import *


def findPairBF(listPoint, countEuclid):
    minDistance, countEuclid = euclidDistance(
        listPoint[0], listPoint[1], countEuclid)
    countEuclid = 0
    minPoint1 = [[0]]
    minPoint2 = [[0]]
    for i in range(len(listPoint)):
        for j in range(i+1, len(listPoint)):
            dis, countEuclid = euclidDistance(
                listPoint[i], listPoint[j], countEuclid)
            if (minDistance == dis):
                minPoint1.append(listPoint[i])
                minPoint2.append(listPoint[j])
            elif (minDistance > dis):
                minDistance = dis
                minPoint1 = [listPoint[i]]
                minPoint2 = [listPoint[j]]

            '''
                print("-----------")
            print(minDistance)
            printPoint(minPoint1)
            printPoint(minPoint2)
            '''

    return minDistance, minPoint1, minPoint2, countEuclid

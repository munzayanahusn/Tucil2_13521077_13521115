import math
import numpy
from tools import *

'''
Algoritma Divide Conquer
Divide  : Bagi himpunan titik menjadi 2 bagian seimbang (jumlah titik tiap bagian sama)
Conquer : Solve jika jumlah titik suatu bagian 2 atau 3, cari distance minimum
Combine : Tentukan nilai jarak antar point minimum, terdapat 3 kasus:
          (a) Pasangan titik terdepat terdapat pada bagian kanan (rightPoint)
          (b) Pasangan titik terdepat terdapat pada bagian kiri (leftPoint)
          (c) Pasangan titik terdepat terdapat pada pasangan titik yang dipisahkan garis maya pembagi (midPoint)
'''

# Fungsi menghitung jarak terdekat pasangan titik yang dipisahkan garis pembagi


def middleCompare(distanceMin, leftPoints, rightPoints, point1, point2, midLine, countEuclid):
    inLeftMiddle = []
    inRightMiddle = []
    #rightboundary,cnt = euclidDistance(points[len(points)//2], points[(len(points)+1)//2], countEuclid)
    rightboundary = midLine+distanceMin
    #leftboundary,cnt2 = euclidDistance(points[len(points)//2], points[(len(points)-1)//2], countEuclid)
    leftboundary = midLine-distanceMin
    # print("boundaries", rightboundary, leftboundary)
    for point in leftPoints:
        if leftboundary <= point[0] <= midLine:
            inLeftMiddle.append(point)
    for point in rightPoints:
        if midLine <= point[0] <= rightboundary:
            inRightMiddle.append(point)

    # print(inLeftMiddle, inRightMiddle)
    # print()

    for i in range(len(inLeftMiddle)):
        for j in range(len(inRightMiddle)):
            distanceNow, countEuclid = euclidDistance(
                inLeftMiddle[i], inRightMiddle[j], countEuclid)

            '''
            print("\n-- Middle --")
            print(distanceNow)
            print(inRightMiddle[j])
            print(inLeftMiddle[i])
            print()
            '''

            if (distanceMin == distanceNow):
                point1.append(inLeftMiddle[i])
                point2.append(inRightMiddle[j])
            elif distanceMin > distanceNow:
                point1 = [inLeftMiddle[i]]
                point2 = [inRightMiddle[j]]
                distanceMin = distanceNow

    return distanceMin, point1, point2, countEuclid

# Menemukan pasangan titik dengan jarak terdekat


def findPairDC(point, countEuclid):

    '''
    print("\n+++++++++++")
    print(point)
    print("+++++++++++\n")
    '''

    # Proses Conquer / solve
    if (len(point) == 2):
        minDistance, countEuclid = euclidDistance(
            point[0], point[1], countEuclid)
        minPoint1 = [point[0]]
        minPoint2 = [point[1]]
    elif (len(point) == 3):
        # Compare P0 dan P1
        minDistance, countEuclid = euclidDistance(
            point[0], point[1], countEuclid)
        minPoint1 = [point[0]]
        minPoint2 = [point[1]]

        # Compare P0 dan P2
        tempDistance, countEuclid = euclidDistance(
            point[0], point[2], countEuclid)
        if (minDistance == tempDistance):
            minPoint1.append(point[0])
            minPoint2.append(point[2])
        elif (minDistance > tempDistance):
            minDistance = tempDistance
            minPoint1 = [point[0]]
            minPoint2 = [point[2]]

        # Compare P1 dan P2
        tempDistance, countEuclid = euclidDistance(
            point[1], point[2], countEuclid)
        if (minDistance == tempDistance):
            minPoint1.append(point[1])
            minPoint2.append(point[2])
        elif (minDistance > tempDistance):
            minDistance = tempDistance
            minPoint1 = [point[1]]
            minPoint2 = [point[2]]
    else:
        # Proses Divide
        leftPoint = point[:(len(point)//2)]
        rightPoint = point[((len(point)//2)):]
        midPoint = (leftPoint[len(leftPoint)-1][0] + rightPoint[0][0])/2
        leftDistance, leftPoint1, leftPoint2, countEuclid = findPairDC(
            leftPoint, countEuclid)
        rightDistance, rightPoint1, rightPoint2, countEuclid = findPairDC(
            rightPoint, countEuclid)

        # Proses Combine
        # print("\n-- Combine --")
        if (leftDistance == rightDistance):
            minDistance = leftDistance
            minPoint1 = leftPoint1 + rightPoint2
            minPoint2 = leftPoint2 + rightPoint2
        elif (leftDistance < rightDistance):
            minDistance = leftDistance
            minPoint1 = leftPoint1
            minPoint2 = leftPoint2
        else:
            minDistance = rightDistance
            minPoint1 = rightPoint1
            minPoint2 = rightPoint2

        '''
        print("----Temp----")
        print(minDistance)
        print(minPoint1)
        print(minPoint2)
        '''

        minDistance, minPoint1, minPoint2, countEuclid = middleCompare(
            minDistance, leftPoint, rightPoint, minPoint1, minPoint2, midPoint, countEuclid)

    '''
    print("-----------")
    print(minDistance)
    print(minPoint1)
    print(minPoint2)
    '''

    return minDistance, minPoint1, minPoint2, countEuclid

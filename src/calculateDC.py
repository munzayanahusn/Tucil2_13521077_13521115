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


def middleCompare(distanceMin, points, point1, point2, indexMid, countEuclid):
    inarroundMiddle = []
    rightboundary = indexMid+int(distanceMin)
    leftboundary = indexMid-int(distanceMin)
    for point in points:
        if point[0] > rightboundary:
            break
        elif leftboundary <= point[0] <= rightboundary:
            inarroundMiddle.append(point)

    for i in range(len(inarroundMiddle)):
        for j in range(i+1, len(inarroundMiddle)):
            distanceNow, countEuclid = euclidDistance(
                inarroundMiddle[i], inarroundMiddle[j], countEuclid)

            if (distanceMin == distanceNow):
                point1.append(inarroundMiddle[i])
                point2.append(inarroundMiddle[j])
            elif distanceMin > distanceNow:
                point1 = [inarroundMiddle[i]]
                point2 = [inarroundMiddle[j]]
                distanceMin = distanceNow

    return distanceMin, point1, point2, countEuclid

# Menemukan pasangan titik dengan jarak terdekat


def findPairDC(point, countEuclid):
    '''
    print("+++++++++++")
    print(point)
    print("+++++++++++")
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
        midPoint = point[len(point)//2][0]
        leftDistance, leftPoint1, leftPoint2, countEuclid = findPairDC(
            leftPoint, countEuclid)
        rightDistance, rightPoint1, rightPoint2, countEuclid = findPairDC(
            rightPoint, countEuclid)

        # Proses Combine
        # print("\n-- Combine --\n")
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

        minDistance, minPoint1, minPoint2, countEuclid = middleCompare(
            minDistance, point, minPoint1, minPoint2, midPoint, countEuclid)

    '''
    print("-----------")
    print(minDistance)
    printPoint(minPoint1)
    printPoint(minPoint2)
    '''
    return minDistance, minPoint1, minPoint2, countEuclid

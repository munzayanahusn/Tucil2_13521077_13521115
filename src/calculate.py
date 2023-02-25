import math
import numpy

'''
Algoritma Divide Conquer
Divide  : Bagi himpunan titik menjadi 2 bagian seimbang (jumlah titik tiap bagian sama)
Conquer : Solve jika jumlah titik suatu bagian 2 atau 3, cari distance minimum
Combine : Tentukan nilai jarak antar point minimum, terdapat 3 kasus:
          (a) Pasangan titik terdepat terdapat pada bagian kanan (rightPoint)
          (b) Pasangan titik terdepat terdapat pada bagian kiri (leftPoint)
          (c) Pasangan titik terdepat terdapat pada pasangan titik yang dipisahkan garis maya pembagi (midPoint)
'''


# Inisiasi variabel global minimum distance dan point
minDistance = 0
minPoint1 = 0
minPoint2 = 0

# Function menghitung euclidean distance


def euclidDistance(point):
    dis = 0
    for i in range(len(point)):
        temp = point[i][0]
        for j in range(1, len(point[i])):
            temp -= point[i][j]
        dis += math.pow(temp, 2)

    return math.sqrt(dis)

# Function menentukan minimum distance kasus 3
# def midPointDistance()


def findPair(point):
    # Proses Conquer / solve
    if (len(point) == 2):
        minDistance = euclidDistance(point)
        minPoint1 = point[0]
        minPoint2 = point[1]
    elif (len(point) == 3):
        # Compare P0 dan P1
        tempPoint = [point[0], point[1]]
        minDistance = euclidDistance(tempPoint)
        minPoint1 = tempPoint[0]
        minPoint2 = tempPoint[1]

        # Compare P0 dan P2
        tempPoint = [point[0], point[2]]
        tempDistance = euclidDistance(tempPoint)
        if (minDistance > tempDistance):
            minDistance = tempDistance
            minPoint1 = tempPoint[0]
            minPoint2 = tempPoint[1]

        # Compare P1 dan P2
        tempPoint = [point[1], point[2]]
        tempDistance = euclidDistance(tempPoint)
        if (minDistance > tempDistance):
            minDistance = tempDistance
            minPoint1 = tempPoint[0]
            minPoint2 = tempPoint[1]
    else:
        # Proses Divide
        leftPoint = point[:(len(point)//2)]
        rightPoint = point[((len(point)//2) + 1):]
        leftDistance = findPair(leftPoint)
        rightDistance = findPair(rightPoint)

        # Proses Combine
        minDistance = min(leftDistance, rightDistance)
        # minDistance = min(minDistance, midPointDistance)

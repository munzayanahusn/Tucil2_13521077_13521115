import math
import numpy

countEuclid = 0

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

# Function menghitung euclidean distance
def euclidDistance(point1, point2):
    global countEuclid
    countEuclid += 1
    print(countEuclid)
    dis = 0
    for i in range(len(point1)):
        temp = point2[i] - point1[i]
        dis += math.pow(temp, 2)

    return math.sqrt(dis)

# Function menentukan minimum distance kasus 3
# def midPointDistance()

#

# Menemukan pasangan titik dengan jarak terdekat


def findPair(point):
    # Proses Conquer / solve
    if (len(point) == 2):
        minDistance = euclidDistance(point[0], point[1])
        minPoint1 = point[0]
        minPoint2 = point[1]
    elif (len(point) == 3):
        # Compare P0 dan P1
        minDistance = euclidDistance(point[0], point[1])
        minPoint1 = point[0]
        minPoint2 = point[1]

        # Compare P0 dan P2
        tempDistance = euclidDistance(point[0], point[2])
        if (minDistance > tempDistance):
            minDistance = tempDistance
            minPoint1 = point[0]
            minPoint2 = point[2]

        # Compare P1 dan P2
        tempDistance = euclidDistance(point[1], point[2])
        if (minDistance > tempDistance):
            minDistance = tempDistance
            minPoint1 = point[1]
            minPoint2 = point[2]
    else:
        # Proses Divide
        leftPoint = point[:(len(point)//2)]
        rightPoint = point[((len(point)//2) + 1):]
        leftDistance, leftPoint1, leftPoint2 = findPair(leftPoint)
        rightDistance, rightPoint1, rightPoint2 = findPair(rightPoint)

        # Proses Combine
        if (leftDistance < rightDistance):
            minDistance = leftDistance
            minPoint1 = leftPoint1
            minPoint2 = leftPoint2
        else:
            minDistance = rightDistance
            minPoint1 = rightPoint1
            minPoint2 = rightPoint2

    return minDistance, minPoint1, minPoint2

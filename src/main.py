import math
from makePoint import *
from calculate import *
import time
from plot import *


countEuclid = 0

# Mengurutkan point berdasarkan nilai sumbu x
# Perlu ga

# Formatting output point


def printPoint(point):
    print("(", end='')
    for i in range(len(point)):
        print(point[i], end='')
        if (i == len(point) - 1):
            print(")")
        else:
            print(", ", end='')


# Main Program
# Jumlah titik atau point
print("Masukkan jumlah titik : ", end='')
n = int(input())
start = time.time()
point = randomPoint(n)    # Menghasilkan array of point
point.sort()
minDistance, minPoint1, minPoint2 = findPair(point)

# Menghitung Waktu Eksekusi
exeTime = time.time() - start
# print(point)


# Output Program
print("Titik Terdekat :")
print("   Titik 1 : ", end='')
printPoint(minPoint1)
print("   Titik 2 : ", end='')
printPoint(minPoint2)
print("   Jarak   :", minDistance, "")
print("Banyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTime)
# Visualisasi
drawPlot(point, minPoint1, minPoint2)

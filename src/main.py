import math
from tools import *
from calculateDC import *
from calculateBruteForce import *
import time
from plot import *

# Main Program
# Jumlah titik atau point
print("Masukkan dimensi vektor : ", end='')
d = int(input())
while (d <= 0):
    print("Input salah! Dimensi harus Bilangan Asli")
    print("Masukkan dimensi vektor : ", end='')
    d = int(input())

print("Masukkan jumlah titik : ", end='')
n = int(input())
while (n <= 1):
    print("Input salah! Banyak titik minimum 2")
    print("Masukkan jumlah titik : ", end='')
    n = int(input())

point = randomPoint(n, d)    # Menghasilkan array of point
point.sort()

minDistance = 0
minPoint1 = []
minPoint2 = []
# Pencarian Pasangan Titik Terdekat dengan Algoritma BruteForce
startBF = time.time()
minDistance, minPoint1, minPoint2, countEuclid = findPairBF(point, 0)

# Menghitung Waktu Eksekusi
exeTimeBF = time.time() - startBF

# Output Program
print("==== ALGORITMA BRUTE FORCE ====")
print("Titik Terdekat :")
print("   Titik 1 : ", end='')
printPoint(minPoint1)
print("   Titik 2 : ", end='')
printPoint(minPoint2)
print("   Jarak   :", minDistance, "")
print("Banyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTimeBF)


minDistance = 0
minPoint1 = []
minPoint2 = []
# Pencarian Pasangan Titik Terdekat dengan Algoritma Divide and Conquer
startDC = time.time()
minDistance, minPoint1, minPoint2, countEuclid = findPairDC(point, 0)

# Menghitung Waktu Eksekusi
exeTimeDC = time.time() - startDC

# Output Program
print("\n==== ALGORITMA DIVIDE AND CONQUER ====")
print("Titik Terdekat :")
print("   Titik 1 : ", end='')
printPoint(minPoint1)
print("   Titik 2 : ", end='')
printPoint(minPoint2)
print("   Jarak   :", minDistance, "")
print("Banyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTimeDC)
# Visualisasi
if(d == 3):
    drawPlot(point, minPoint1, minPoint2)

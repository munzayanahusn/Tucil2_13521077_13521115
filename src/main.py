import math
from tools import *
from calculateDC import *
from calculateBruteForce import *
import time
from plot import *
from quickSortSbX import *

# Main Program
# Print Splash Screen

print("\n")
print("     𝑭 𝒊 𝒏 𝒅   𝑻 𝒉 𝒆\n")
print("     ░█▀▀█ █── █▀▀█ █▀▀ █▀▀ █▀▀ ▀▀█▀▀    ░█▀▀█ █▀▀█ ─▀─ █▀▀█ ")
print("     ░█─── █── █──█ ▀▀█ █▀▀ ▀▀█ ──█──    ░█▄▄█ █▄▄█ ▀█▀ █▄▄▀ ")
print("     ░█▄▄█ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ──▀──    ░█─── ▀──▀ ▀▀▀ ▀─▀▀ \n")

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


# 0.017321

point = randomPoint(n, d)    # Menghasilkan array of point
point.append([0, 0, 0])
point.append([1, 1, 1])
point.append([2, 2, 2])
point.append([3, 3, 3])
point.append([4, 4, 4])
point = quickSortSbX(point, 0, len(point)-1)

minDistance = 0
minPoint1 = [[0]]
minPoint2 = [[0]]
# Pencarian Pasangan Titik Terdekat dengan Algoritma BruteForce
startBF = time.time()
minDistance, minPoint1, minPoint2, countEuclid = findPairBF(point, 0)

# Menghitung Waktu Eksekusi
exeTimeBF = time.time() - startBF

# Output Program
print("\n\n==== ALGORITMA BRUTE FORCE ====")
print("Terdapat", len(minPoint1), "pasang titik terdekat !")
print(minPoint1)
print(minPoint2)
print("Jarak pasangan titik terdekat :", minDistance)
for i in range(len(minPoint1)):
    print("Pasangan Titik Terdekat ke-", (i+1), " :")
    print("   Titik 1 : ", end='')
    printPoint(minPoint1[i])
    print("   Titik 2 : ", end='')
    printPoint(minPoint2[i])
print("Banyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTimeBF)
print("\n")


minDistance = 0
minPoint1 = [[0]]
minPoint2 = [[0]]
# Pencarian Pasangan Titik Terdekat dengan Algoritma Divide and Conquer
startDC = time.time()
minDistance, minPoint1, minPoint2, countEuclid = findPairDC(point, 0)

# Menghitung Waktu Eksekusi
exeTimeDC = time.time() - startDC

# Output Program
print("\n==== ALGORITMA DIVIDE AND CONQUER ====")
print("Terdapat", len(minPoint1), "pasang titik terdekat !")
print(minPoint1)
print(minPoint2)
print("Jarak pasangan titik terdekat :", minDistance)
for i in range(len(minPoint1)):
    print("Pasangan Titik Terdekat ke-", (i+1), " :")
    print("   Titik 1 : ", end='')
    printPoint(minPoint1[i])
    print("   Titik 2 : ", end='')
    printPoint(minPoint2[i])
print("Banyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTimeDC)
# Visualisasi
if(d == 3):
    drawPlot(point, minPoint1, minPoint2)

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
print("\033[36m     ░█▀▀█ █── █▀▀█ █▀▀ █▀▀ █▀▀ ▀▀█▀▀    ░█▀▀█ █▀▀█ ─▀─ █▀▀█ ")
print("     ░█─── █── █──█ ▀▀█ █▀▀ ▀▀█ ──█──    ░█▄▄█ █▄▄█ ▀█▀ █▄▄▀ ")
print("     ░█▄▄█ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ──▀──    ░█─── ▀──▀ ▀▀▀ ▀─▀▀ \n\033[0m")

# Jumlah titik atau point
print("Masukkan \033[01mdimensi vektor : \033[0m", end='')
d = int(input())
while (d <= 0):
    print("\033[1m\033[91m     Input salah! Dimensi harus Bilangan Asli\033[0m\n")
    print("Masukkan \033[1mdimensi vektor : \033[0m", end='')
    d = int(input())

print("Masukkan \033[01mjumlah titik : \033[0m", end='')
n = int(input())
while (n <= 1):
    print("\033[1m \033[91m     Input salah! Banyak titik minimum 2 \033[0m\n")
    print("Masukkan \033[1m jumlah titik : \033[0m", end='')
    n = int(input())

print()
proc = '\033[01m\033[33mProcessing ...\033[0m'
for i in proc:
    print(i, end='')
    time.sleep(0.3)
print("\n")

point = randomPoint(n, d)    # Menghasilkan array of point
# point.append([0, 0, 0])

point = quickSortSbX(point, 0, len(point)-1)

# Pencarian Pasangan Titik Terdekat dengan Algoritma BruteForce
startBF = time.time()
minDistance, minPoint1, minPoint2, countEuclid = findPairBF(point, 0)

# Menghitung Waktu Eksekusi
exeTimeBF = time.time() - startBF

# Output Program
print("\033[1m\033[95m==== ALGORITMA BRUTE FORCE ====\033[0m")
print("\033[95mTerdapat\033[01m", len(minPoint1),
      "pasang \033[0m\033[95mtitik terdekat !")
print("Jarak pasangan titik terdekat :", minDistance, "satuan jarak\033[0m")
for i in range(len(minPoint1)):
    print("\nPasangan Titik Terdekat ke-", (i+1), " :")
    print("   Titik 1 : ", end='')
    printPoint(minPoint1[i])
    print("   Titik 2 : ", end='')
    printPoint(minPoint2[i])
print("\n\033[95mBanyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTimeBF, "\033[0m")


# Pencarian Pasangan Titik Terdekat dengan Algoritma Divide and Conquer
startDC = time.time()
minDistance, minPoint1, minPoint2, countEuclid = findPairDC(point, 0)

# Menghitung Waktu Eksekusi
exeTimeDC = time.time() - startDC

# Output Program
print(
    "\n\033[1m\033[92m==== ALGORITMA DIVIDE AND CONQUER ====\033[0m")
print("\033[92mTerdapat\033[01m", len(minPoint1),
      "pasang \033[0m\033[92mtitik terdekat !")
print("Jarak pasangan titik terdekat :", minDistance, "satuan jarak\033[0m")
for i in range(len(minPoint1)):
    print("\nPasangan Titik Terdekat ke-", (i+1), " :")
    print("   Titik 1 : ", end='')
    printPoint(minPoint1[i])
    print("   Titik 2 : ", end='')
    printPoint(minPoint2[i])
print("\n\033[32mBanyak Perhitungan Jarak Euclidean Distance :", countEuclid)
print("Execution Time : %s seconds" % exeTimeDC, "\033[0m")

# Visualisasi
if(d == 3):
    print("\n\033[01m\033[33mShow 3D Visualization ...\033[0m")
    drawPlotResult(minPoint1, minPoint2)
    drawPlot(point, minPoint1, minPoint2)

print()

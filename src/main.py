import math
import makePoint
import calculate

# Mengurutkan point berdasarkan nilai sumbu x
# Perlu ga

n = int(input())                    # Jumlah titik atau point
point = makePoint.randomPoint(n)    # Menghasilkan array of point
point.sort()
# calculate.findPair(point)
print(point)

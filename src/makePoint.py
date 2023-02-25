import math
import random

# Fungsi randomize point
def randomPoint(n):
    point = []
    for i in range(n):
        temp = [round(random.uniform(-100, 100), 2), 
                round(random.uniform(-100, 100), 2),
                round(random.uniform(-100, 100), 2)]
        point.append(temp)
    return point
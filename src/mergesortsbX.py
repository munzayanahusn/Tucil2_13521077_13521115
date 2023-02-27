#MergeSort, karena elemen terdiri dari x,y,z fungsi ini hanya akan mengurutkan elemen berdasarkan  sb-x
def mergeSortSbX(points):
    if len(points) > 1:
        #Proses Membagi 2 array
        idxMiddle = len(points)//2
        leftPoints = points[:idxMiddle]
        rightPoints = points[idxMiddle:]
        #Proses rekursif
        mergeSortSbX(leftPoints)
        mergeSortSbX(rightPoints)
        idx = 0
        leftidx = 0
        rightidx = 0
        #Proses Sorting
        while rightidx < len(rightPoints) and leftidx < len(leftPoints):
            if rightPoints[rightidx][0] < leftPoints[leftidx][0]:
                points[idx] = rightPoints[rightidx]
                rightidx += 1
            elif rightPoints[rightidx][0] > leftPoints[leftidx][0]:
                points[idx] = leftPoints[leftidx]
                leftidx += 1
            idx += 1
        while rightidx < len(rightPoints):
            points[idx] = rightPoints[rightidx]
            rightidx += 1
            idx += 1
        while leftidx < len(leftPoints):
            points[idx] = leftPoints[leftidx]
            leftidx += 1
            idx += 1

    return points


'''if __name__ == '__main__':
    array = [[6,1,2],[2,5,1],[12, 10, 9],[15,22,21]]

    array = mergeSortSbX(array)
    print(array)'''
    

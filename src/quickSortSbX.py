#Fungsi sort dengan Quick Sort Menggunakan Divide And Conquer
#Diurutkan berdasarkan sb-X dari kecil ke besar

#Pivot yang digunakan adalah elemen terakhir dari array 
def partitionSort(point,idxInit,idxLast):
   #Pivot elemen terakhir array
   pivot = point[idxLast][0]
   #Bagian ini mempartisi dengan cara nilai-nilai yang lebih kecil dari pivot ditaruh
   #dibagian paling kiri dan nilai yang lebih besar dari pivot ditaruh di bagian kanan pivot
   #nilai pertama yang ditemui lebih kecil dari pivot akan ditaruh paling ujung kiri dan seterusnya
   #Fungsi mereturn nilai dimana partisi telah berhenti dilakukan
   i = idxInit-1
   for j in range(idxInit,idxLast):
      if point[j][0] <= pivot:
        i = i+1
        point[i],point[j] = point[j],point[i]  #Bagian swap
   point[i+1],point[idxLast] = point[idxLast],point[i+1]
   return ( i+1 )
#Main quick sort
def quickSortSbX(point,idxInit,idxLast):
   if idxInit < idxLast:
      partisi = partitionSort(point, idxInit, idxLast)
      quickSortSbX(point, idxInit, partisi-1)       #rekursif bagian kiri array
      quickSortSbX(point, partisi+1, idxLast)       #rekursif bagian kanan array
   return point





'''if __name__ == '__main__':
    array = [[6,1,2],[2, 10, 9],[1,5,1]]

    array = quickSortSbX(array, 0, len(array)-1)
    print(array)
    '''

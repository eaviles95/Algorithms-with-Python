#Bubblesort algorithm

disorderedList = [4, 3, 5, 6, 7, 0, 2, 7, 9]

def changeData(arrayList, i, j):
  if i != j:
    aux = arrayList[i]
    arrayList[i] = arrayList[j]
    arrayList[j] = aux
    return arrayList
  
def bubbleSort(arrayList):
  n = len(arrayList)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if arrayList[j] > arrayList[j+1]:
        arrayList = changeData(arrayList, j, j+1)
  return arrayList

print(bubbleSort(disorderedList))


  

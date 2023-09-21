# Selection sort

disorderedList = [4, 3, 5, 6, 7, 0, 2, 7, 9]

def changeData(arrayList, i, j):
  if i != j:
    aux = arrayList[i]
    arrayList[i] = arrayList[j]
    arrayList[j] = aux
    return arrayList

def selectionSort(arrayList):
  n = len(arrayList)
  for i in range(0, n-2):
    bestIndex = i
    bestValue = arrayList[i]
    for j in range(i+1, n-1):
      if arrayList[j]< bestValue:
        bestIndex = j
        bestValue = arrayList[j]
    if bestIndex != i:
      arrayList = changeData(arrayList, i, bestIndex)
  return arrayList

print(selectionSort(disorderedList))

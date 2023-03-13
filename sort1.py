def quickSort(L):
    if (len(L) < 1):
        return L
    mid = len(L)//2
    pivot = L[mid]
    left = []
    right = []
    for i in range(len(L)):
        if(i == mid):
            continue
        if(L[i] < pivot):
            left.append(L[i])
        else:
            right.append(L[i])
    left = quickSort(left)
    right = quickSort(right)

    return left + [pivot] + right

def mergeSort(L):
    if (len(L) > 1):
        meio = len(L)//2
        left = L[:meio]
        right = L[meio:]
        i = 0
        k = 0
        j = 0
        mergeSort(left)
        mergeSort(right)

        while k < len(left) and j < len(right):
            if(left[k] < right[i]):
                L[i] = left[k]
                k +=1 
            else:
                L[i] = left[j]
                j +=1
            i+=1

        while k < len(left):
            L[i] = left[k]
            k+=1
            i+=1
        while j < len(right):
            L[i] = left[j]
            j+=1
            i+=1
     
L = [9,8,7,4,5,2,3,1,6]
print("Lista Desordenada: ",L)
sortedL = mergeSort(L)
print("Lista Ordenada: ",sortedL)


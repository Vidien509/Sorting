def selectionSort(L,i,j,count):
    if(i == j):
        print("Lista Ordenada: ",L)
        print("Número de Comparações: ",count+1)
        return L
    if (L[i] >= L[j]):
        L[i], L[j] = L[j], L[i]
        selectionSort(L,i,j-1,count+1)
    else:
        if(j > i+1):
            selectionSort(L,i,j-1,count+1) 
        else:
            selectionSort(L,i+1,len(L)-1,count+1)
            
L = [9,8,7,4,5,2,3,1,6]
j = len(L)-1
count = 0
print("Lista Desordenada: ",L)
selectionSort(L,0,j,count)
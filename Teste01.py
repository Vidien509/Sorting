def selectionSort(L):
    for i in range(0,len(L)-1):
        menor = i
        for j in range(i+1,len(L)):
            if L[j] <= L[menor]:
                menor = j
        L[i], L[menor] = L[menor], L[i]
    return L

L = [9,8,7,6,5,4,3,2,1]

def selSortRec(L,i,j):
    if (j < len(L)-1):
        j -= 1
    print (L[i])
    print ("j = ",L[j])
    if L[i+1] >= L[j] and i < len(L)-2:
        L[i], L[j] = L[j], L[i]
        i += 1
        selSortRec(L,i,j)
    else:
        if(i < len(L)-2):
            selSortRec(L,i,j)
        print(L)
        return L
    

selSortRec(L,-1,len(L)-1)
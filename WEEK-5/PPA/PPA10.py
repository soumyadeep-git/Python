def insert(L, x):
    L.append(x)
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
    return L
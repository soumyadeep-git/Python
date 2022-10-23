def type_of_sequence(L):
    k=0
    for i in range(len(L)):
        if mysterious(L[i]):
            k+=1
    if k<2:
        return 'mildly mysterious'
    elif k<5:
        return 'moderately mysterious'
    else:
        return 'most mysterious'
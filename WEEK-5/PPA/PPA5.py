def first_three(L):
    fmax=-10000
    smax=-10000
    tmax=-10000
    for i in range(len(L)):
        if L[i]>fmax:
            fmax,smax,tmax=L[i],fmax,smax
        elif L[i]>smax:
            smax,tmax=L[i],smax
        elif L[i]>tmax:
            tmax=L[i]
    return fmax,smax,tmax
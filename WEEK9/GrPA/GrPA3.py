def get_goals(filename, country):
    f=open(filename,'r')
    l=f.readlines()[1:]
    c=-1
    g=-1
    for i in l:
        if country in i:
            t = i.split(',')
            if c == -1:
                c=1
                g = int(t[2])
            else:
                c+=1
                g+=int(t[2])
    f.close()
    return((c,g))
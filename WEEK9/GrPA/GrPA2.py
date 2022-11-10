def relation(file1,file2):
    f1 = open(file1,'r')
    f2 = open(file2,'r')
    l1= f1.readlines()
    l2 =f2.readlines()
    f1.close()
    f2.close()
    flag = True
    if l1==l2:
        return'Equal'
    else:
        for i in range(len(l1)):
            if l1[i] not in l2[i]:
                flag = False
    if flag:
        return'Subset'
    else:
        return'No Relation'
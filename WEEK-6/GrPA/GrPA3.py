def rotate(mat):
#print(mat)
    rotated=[]
    for i in range(len(mat[0])):
        turned=[]
        for j in mat[::-1]:
        #print(j[i])
            turned.append(j[i])
        rotated.append(turned)
    return rotated
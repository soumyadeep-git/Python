def get_column(mat, col):
    l=[]
    for i in range(len(mat)):
        l.append(mat[i][col])
    return l
def get_row(mat, row):
    l=[]
    for i in range(len(mat[0])):
        l.append(mat[row][i])
    return l
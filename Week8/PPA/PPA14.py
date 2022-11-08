def minor_matrix(M, col):
    n = len(M)
    M_ij = [ ]
    for i in range(1, n):
        L = [ ]
        for j in range(n):
            if j == col:
                continue
            L.append(M[i][j])
        M_ij.append(L)
    return M_ij
def det(M):
    n = len(M)
    if n == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    dsum = 0
    for j in range(n):
        dsum = dsum + M[0][j] * det(minor_matrix(M, j)) * ((-1) ** (j))
    return dsum
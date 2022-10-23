# Return YES if the diagonal, row and column sum of a matirx are same.

def is_magic(mat):
    # first get the dimensions of the matrix.
    dim = len(mat)
    # the sum of the diagonals
    d1sum, d2sum = 0, 0
    # [i], [i] gives us the forward diagonal and [i], [m-i-1] gives us the backward diagonal.
    for i in range(dim):
        d1sum = d1sum+mat[i][i]
        d2sum = d2sum+mat[i][dim-i-1]
    # if the two diagonal sum are unequal then we can rule out some unneccesary calculations.
    if(d1sum!= d2sum):
        return 'NO'
    # Now the rows and columns sum
    for i in range(dim):
        rsum, csum = 0, 0
        for j in range(dim):
            rsum = rsum+mat[i][j]
            csum = csum+mat[j][i]
        if not rsum == csum:
            return 'NO'
    # If the code reaches here i.e, it has met all the conditions.
    return 'YES'

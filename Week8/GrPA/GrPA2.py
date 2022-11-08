def linear(P, Q, k):
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[0] / Q[0] != k:
        return False
    return linear(P[1: ], Q[1: ], k)
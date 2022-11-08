def subset_sum(L, s):
    if s == 0:
        return True
    if len(L) == 0:
        return False
    if subset_sum(L[:-1], s - L[-1]):
        return True
    else:
        return subset_sum(L[:-1], s)
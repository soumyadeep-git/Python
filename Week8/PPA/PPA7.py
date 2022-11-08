def count(L, word):
    if len(L) == 0:
        return 0
    if L[-1] == word:
        return 1 + count(L[:-1], word)
    else:
        return count(L[:-1], word)
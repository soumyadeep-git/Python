def is_key(D, key):
    return key in D
def value(D, key):
    if is_key(D, key):
        return D[key]
    else:
        return None
print(value({'good': 4, 'day': 3}, 'day'))
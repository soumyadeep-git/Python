def value_to_keys(D, value):
    values = [ ]
    for key in D:
        if D[key] == value:
            values.append(key)
    return values
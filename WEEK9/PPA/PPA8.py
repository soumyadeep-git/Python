def improvement(filename):
    f = open(filename, 'r')
    f.readline()
    count = 0
    for line in f:
        name, gender, ct, python, pdsa = line.strip().split(',')
        ct, python, pdsa = int(ct), int(python), int(pdsa)
        if ct < python < pdsa:
            count += 1
    f.close()
    return count
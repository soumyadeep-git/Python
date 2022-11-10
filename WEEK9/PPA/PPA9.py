def extract_lines(filename):
    f = open(filename, 'r')
    header = f.readline()
    g = open('python.csv', 'w')
    g.write(header)
    for line in f:
        L = line.strip().split(',')
        python = int(L[4])
        gender = L[2]
        if gender == 'M' and python >= 70:
            g.write(line)
    f.close()
    g.close()
def add_period(filename):
    f = open(filename, 'r')
    g = open('out.txt', 'w')
    for line in f:
        line = line.strip()
        g.write(line + '.' + '\n')
    f.close()
    g.close()
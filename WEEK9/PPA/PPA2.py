def read_line(filename, n):
    f = open(filename, 'r')
    count = 0
    line = f.readline()
    while line != '':
        count += 1
        line = line.strip()
        if count == n:
            return line
        line = f.readline()
    f.close()
    return None
def read_file(filename):
    f = open(filename, 'r')
    for line in f:
        print(line.strip())
    f.close()
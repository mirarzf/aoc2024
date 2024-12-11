def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    line = [int(e) for e in f.read().split(' ')]
    f.close()

    return 0
def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    nrow, ncols = len(lines), len(lines[0])

    # Create dictionary of all antennas types and their positions 
    antennas = {}
    for i, line in enumerate(lines): 
        for j, c in enumerate(line): 
            if c != '.': 
                antennaType = c
                if antennaType in antennas.keys(): 
                    antennas[antennaType].append((i, j))
                else: 
                    antennas[antennaType] = [(i,j)]
    
    print(antennas)

    somme = 0
    for line in lines: 
        somme += 1

    return somme
def isValidPos(pos, nrows, ncols): 
    i, j = pos 
    return i >= 0 and i < nrows and j >= 0 and j < ncols

def getAntinodePosition(pos1, pos2): 
    if pos1 == pos2: 
        return -1, -1 
    
    deltaI = pos2[0]-pos1[0]
    deltaJ = pos2[1]-pos1[1]

    return pos1[0]-deltaI, pos1[1]-deltaJ

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    nrows, ncols = len(lines), len(lines[0])

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
    
    # Create antinodes 
    antinodesPositions = []
    for antennaType in antennas.keys(): 
        for antenna1 in antennas[antennaType]: 
            for antenna2 in antennas[antennaType]: 
                antinodePos = getAntinodePosition(antenna1, antenna2)
                if isValidPos(antinodePos, nrows, ncols): 
                    antinodesPositions.append(antinodePos)

    return len(set(antinodesPositions))
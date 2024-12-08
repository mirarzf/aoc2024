from math import gcd

def isValidPos(pos, nrows, ncols): 
    i, j = pos 
    return i >= 0 and i < nrows and j >= 0 and j < ncols

def getAntinodePositions(pos1, pos2, puzzlepart, nrows, ncols):     
    deltaI = pos2[0]-pos1[0]
    deltaJ = pos2[1]-pos1[1]
    pgcdDeltaS = gcd(deltaI, deltaJ)

    listpos = []
    if puzzlepart == 1: 
        antinodePos1 = (pos1[0]-deltaI, pos1[1]-deltaJ)
        if isValidPos(antinodePos1, nrows, ncols): 
            listpos.append(antinodePos1)
        antinodePos2 = (pos2[0]+deltaI, pos2[1]+deltaJ)
        if isValidPos(antinodePos2, nrows, ncols): 
            listpos.append(antinodePos2)
    else: 
        k = 0 
        antinodePos = (pos1[0]-k*deltaI, pos1[1]-k*deltaJ)
        while isValidPos(antinodePos, nrows, ncols): 
            listpos.append(antinodePos)
            antinodePos = (pos2[0]-k*deltaI, pos2[1]-k*deltaJ)
            k += 1
        k = 1
        antinodePos = (pos1[0]+k*deltaI, pos1[1]+k*deltaJ)
        while isValidPos(antinodePos, nrows, ncols): 
            listpos.append(antinodePos)
            antinodePos = (pos1[0]+k*deltaI, pos1[1]+k*deltaJ)
            k += 1
    return listpos

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
        for i, antenna1 in enumerate(antennas[antennaType]): 
            for antenna2 in antennas[antennaType][i+1:]: 
                multiAntinodePos = getAntinodePositions(antenna1, antenna2, puzzlepart, nrows, ncols)
                antinodesPositions += multiAntinodePos

    return len(set(antinodesPositions))
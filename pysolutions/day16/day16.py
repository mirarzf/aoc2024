import numpy as np 

def getNeighbours(pos, grid, distances, directions): 
    i, j = pos 
    currDistV = distances['V'][i,j]
    currDistH = distances['H'][i,j]
    nrows, ncols = len(grid), len(grid[0])
    neighbours = []

    # GO UP 
    if i > 0 and grid[i-1][j] != '#': 
        row, col = i-1, j
        dist = distances['V'][row,col]

        tempDistV = currDistV+1
        tempDistH = currDistH+1001
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['V'][row,col] = tempDist
            neighbours.append((row,col))
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        
    # GO DOWN 
    if i < nrows-1 and grid[i+1][j] != '#': 
        row, col = i+1, j
        dist = distances['V'][row,col]

        tempDistV = currDistV+1
        tempDistH = currDistH+1001
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['V'][row,col] = tempDist
            neighbours.append((row,col))
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        
    # GO LEFT 
    if j > 0 and grid[i][j-1] != '#': 
        row, col = i, j-1
        dist = distances['H'][row,col]

        tempDistV = currDistV+1001
        tempDistH = currDistH+1
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['H'][row,col] = tempDist
            neighbours.append((row,col))
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        
    # GO RIGHT 
    if j < ncols-1 and grid[i][j+1] != '#': 
        row, col = i, j+1
        dist = distances['H'][row,col]

        tempDistV = currDistV+1001
        tempDistH = currDistH+1
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['H'][row,col] = tempDist
            neighbours.append((row,col))
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        
    return neighbours

def Dijkstra(startPos, grid, isStart = True): 
    nrows, ncols = len(grid), len(grid[0])
    
    distances = {}
    distances['H'] = np.ones((nrows, ncols), dtype = int)*1000000
    distances['V'] = np.ones((nrows, ncols), dtype = int)*1000000
    directions = [['.' for k1 in range(ncols)] for k2 in range(nrows)]
    distances['H'][startPos] = 0
    distances['V'][startPos] = 1000 if isStart else 0 
    directions[startPos[0]][startPos[1]] = 'H'

    neighbours = [startPos]
    while len(neighbours) > 0: 
        neighbour = neighbours.pop()
        neighbours += getNeighbours(neighbour, grid, distances, directions)

    return distances

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()

    startPos, endPos = (0,0), (0,0)

    # Get Start Point and End Point 
    for i, line in enumerate(lines): 
        for j, c in enumerate(line): 
            if c == 'S': 
                startPos = (i,j)
            if c == 'E': 
                endPos = (i,j)
    
    distancesFromStart = Dijkstra(startPos, lines)

    shortestPath = min(distancesFromStart['H'][endPos], distancesFromStart['V'][endPos])
    if puzzlepart == 1: 
        return shortestPath

    distancesFromEnd = Dijkstra(endPos, lines, isStart=False)
    onBestPath = 0 
    for i, line in enumerate(lines): 
        for j, c in enumerate(line): 
            if c != '#': 
                pos = i,j
                pathHH = distancesFromStart['H'][pos]+distancesFromEnd['H'][pos]
                pathVV = distancesFromStart['V'][pos]+distancesFromEnd['V'][pos]
                pathHV = distancesFromStart['H'][pos]+distancesFromEnd['V'][pos]+1000
                pathVH = distancesFromStart['V'][pos]+distancesFromEnd['H'][pos]+1000
                onPath = min(pathHH, pathHV, pathVH, pathVV) <= shortestPath                
                if onPath: 
                    onBestPath += 1 
    return onBestPath
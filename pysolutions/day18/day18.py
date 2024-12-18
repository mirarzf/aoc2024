import numpy as np 

def getNeighbours(pos, grid, distances): 
    i, j = pos 
    currDist = distances[i,j]
    nrows, ncols = grid.shape
    neighbours = []

    # GO UP 
    if i > 0 and grid[i-1,j] == 0: 
        row, col = i-1, j
        dist = distances[row,col]
        if dist > currDist+1: 
            distances[row,col] = currDist+1
            neighbours.append((row,col))
    # GO DOWN 
    if i < nrows-1 and grid[i+1,j] == 0: 
        row, col = i+1, j
        dist = distances[row,col]
        if dist > currDist+1: 
            distances[row,col] = currDist+1
            neighbours.append((row,col))
    # GO LEFT 
    if j > 0 and grid[i,j-1] == 0: 
        row, col = i, j-1
        dist = distances[row,col]
        if dist > currDist+1: 
            distances[row,col] = currDist+1
            neighbours.append((row,col))
    # GO RIGHT 
    if j < ncols-1 and grid[i,j+1] == 0: 
        row, col = i, j+1
        dist = distances[row,col]
        if dist > currDist+1: 
            distances[row,col] = currDist+1
            neighbours.append((row,col))
        
    return neighbours

def getGridAtStep(laststep, lines, gridshape): 
    grid = np.zeros(gridshape, dtype=int)
    for k in range(laststep): 
        line = lines[k]
        grid[int(line[0]), int(line[1])] = 1 
    return grid 

def Dijkstra(startPos, gridshape, lines, bytesLimit): 
    nrows, ncols = gridshape
    nbSteps = 0
    
    distances = np.ones(gridshape, dtype = int)*(nrows*ncols)
    distances[startPos] = 0

    neighbours = [startPos]
    nbSteps = [0]
    grid=getGridAtStep(bytesLimit, lines, gridshape)
    while len(neighbours) > 0: 
        neighbour = neighbours.pop(0)
        newstep = nbSteps.pop(0)
        newNeighbours = getNeighbours(neighbour, grid, distances)
        neighbours += newNeighbours
        nbSteps += [newstep+1 for i in range(len(newNeighbours))]

    return distances

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n').split(',') for line in f.readlines()]
    f.close()

    nrows, ncols, bytesLimit = 71, 71, 1024
    # nrows, ncols, bytesLimit = 7, 7, 12 # FOR TEST 

    startPos, endPos = (0,0), (nrows-1,ncols-1)
    
    distancesFromStart = Dijkstra(startPos, (nrows, ncols), lines, bytesLimit)
    shortestPath = distancesFromStart[endPos]
    if puzzlepart == 1: 
        return shortestPath
    
    while shortestPath != nrows*ncols and bytesLimit < len(lines): 
        bytesLimit += 1 
        shortestPath = Dijkstra(startPos, (nrows, ncols), lines, bytesLimit)[endPos]
    if bytesLimit == len(lines): 
        return f"{lines[-1][0]},{lines[-1][1]}"
    else: 
        return f"{lines[bytesLimit-1][0]},{lines[bytesLimit-1][1]}"
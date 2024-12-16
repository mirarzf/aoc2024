import numpy as np 

def getNeighbours(pos, grid, distances, directions, preds): 
    i, j = pos 
    currDist = distances[i,j]
    currDir = directions[i][j]
    nrows, ncols = len(grid), len(grid[0])
    neighbours = []
    # GO UP 
    if i > 0 and grid[i-1][j] != '#': 
        dist = distances[i-1,j]
        if currDir == 'H': 
            tempDist = currDist+1000+1
        else: 
            tempDist = currDist+1
        if dist > tempDist: 
            distances[i-1,j] = tempDist
            directions[i-1][j] = 'V'
            neighbours.append((i-1,j))
            preds[i-1][j] = (i,j)
    
    # GO DOWN 
    if i < nrows-1 and grid[i+1][j] != '#':  
        dist = distances[i+1,j]
        if currDir == 'H': 
            tempDist = currDist+1000+1
        else: 
            tempDist = currDist+1
        if dist > tempDist: 
            distances[i+1,j] = tempDist
            directions[i+1][j] = 'V'
            neighbours.append((i+1,j))
            preds[i+1][j] = (i,j)

    # GO LEFT 
    if j > 0 and grid[i][j-1] != '#':  
        dist = distances[i,j-1]
        if currDir == 'V': 
            tempDist = currDist+1000+1
        else: 
            tempDist = currDist+1
        if dist > tempDist: 
            distances[i,j-1] = tempDist
            directions[i][j-1] = 'H'
            neighbours.append((i,j-1))
            preds[i][j-1] = (i,j)

    # GO RIGHT 
    if j < ncols-1 and grid[i][j+1] != '#': 
        dist = distances[i,j+1]
        if currDir == 'V': 
            tempDist = currDist+1000+1
        else: 
            tempDist = currDist+1
        if dist > tempDist: 
            distances[i,j+1] = tempDist
            directions[i][j+1] = 'H'
            neighbours.append((i,j+1))
            preds[i][j+1] = (i,j)
    
    return neighbours

def Dijkstra(startPos, grid): 
    nrows, ncols = len(grid), len(grid[0])
    
    distances = np.ones((nrows, ncols), dtype=int)*1000000
    directions = [['.' for k1 in range(ncols)] for k2 in range(nrows)]
    distances[startPos] = 0
    directions[startPos[0]][startPos[1]] = 'H'
    preds = [[(0,0) for k1 in range(ncols)] for k2 in range(nrows)]

    neighbours = [startPos]
    while len(neighbours) > 0: 
        neighbour = neighbours.pop()
        neighbours += getNeighbours(neighbour, grid, distances, directions, preds)

    return distances, preds

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
    print(startPos, endPos)
    
    distances, predecessors = Dijkstra(startPos, lines)

    # i, j = endPos
    # while (i,j) != startPos: 
    #     print((i,j))
    #     i,j = predecessors[i][j]

    return distances[endPos[0], endPos[1]]

#  85440 too high 
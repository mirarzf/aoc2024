import numpy as np 

def getNeighbours(pos, grid, distances, directions, preds): 
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
        tempDistH = currDistH+1000+1
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['V'][row,col] = tempDist
            neighbours.append((row,col))
            preds['V'][row][col] = (i,j)
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        preds['minimum'][row][col] = preds['V'][row][col] if distances['H'][row,col] > distances['V'][row,col] else preds['H'][row][col]

    # GO DOWN 
    if i < nrows-1 and grid[i+1][j] != '#': 
        row, col = i+1, j
        dist = distances['V'][row,col]

        tempDistV = currDistV+1
        tempDistH = currDistH+1000+1
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['V'][row,col] = tempDist
            neighbours.append((row,col))
            preds['V'][row][col] = (i,j)
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        preds['minimum'][row][col] = preds['V'][row][col] if distances['H'][row,col] > distances['V'][row,col] else preds['H'][row][col]

    # GO LEFT 
    if j > 0 and grid[i][j-1] != '#': 
        row, col = i, j-1
        dist = distances['H'][row,col]

        tempDistV = currDistV+1000+1
        tempDistH = currDistH+1
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['H'][row,col] = tempDist
            neighbours.append((row,col))
            preds['H'][row][col] = (i,j)
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        preds['minimum'][row][col] = preds['V'][row][col] if distances['H'][row,col] > distances['V'][row,col] else preds['H'][row][col]

    # GO RIGHT 
    if j < ncols-1 and grid[i][j+1] != '#': 
        row, col = i, j+1
        dist = distances['H'][row,col]

        tempDistV = currDistV+1000+1
        tempDistH = currDistH+1
        tempDist = min(tempDistV, tempDistH)
        if dist > tempDist: 
            distances['H'][row,col] = tempDist
            neighbours.append((row,col))
            preds['H'][row][col] = (i,j)
        
        directions[row][col] = 'V' if distances['H'][row,col] > distances['V'][row,col] else 'H'
        preds['minimum'][row][col] = preds['V'][row][col] if distances['H'][row,col] > distances['V'][row,col] else preds['H'][row][col]
    
    return neighbours

def Dijkstra(startPos, grid): 
    nrows, ncols = len(grid), len(grid[0])
    
    distances = {}
    distances['H'] = np.ones((nrows, ncols), dtype = int)*1000000
    distances['V'] = np.ones((nrows, ncols), dtype = int)*1000000
    directions = [['.' for k1 in range(ncols)] for k2 in range(nrows)]
    distances['H'][startPos] = 0
    distances['V'][startPos] = 1000
    directions[startPos[0]][startPos[1]] = 'H'
    preds = {}
    preds['V'] = [[(0,0) for k1 in range(ncols)] for k2 in range(nrows)]
    preds['H'] = [[(0,0) for k1 in range(ncols)] for k2 in range(nrows)]
    preds['minimum'] = [[(0,0) for k1 in range(ncols)] for k2 in range(nrows)]

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
    
    # countPreds = 0
    # i, j = endPos
    # while (i,j) != startPos: 
    #     countPreds += 1
    #     i,j = predecessors['minimum'][i][j]
    #     print(i,j)
    # print(countPreds)

    return min(distances['H'][endPos], distances['V'][endPos])

# 85440 too high 
# 85355 too low 

# Right test answer is 5024 
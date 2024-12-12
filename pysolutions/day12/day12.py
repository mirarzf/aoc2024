import numpy as np 

def getNeighboursAndNewFences(i, j, grid, visited): 
    neighbours = []
    similarNeighbours = 0 
    if i > 0 and grid[i][j] == grid[i-1][j]: 
        if visited[i-1][j]==0: 
            neighbours.append((i-1,j)) 
        similarNeighbours += 1 
    if i < len(grid)-1 and grid[i][j] == grid[i+1][j]: 
        if visited[i+1][j]==0: 
            neighbours.append((i+1,j)) 
        similarNeighbours += 1 
    if j > 0 and grid[i][j] == grid[i][j-1]:
        if visited[i][j-1]==0: 
            neighbours.append((i,j-1)) 
        similarNeighbours += 1 
    if j < len(grid[0])-1 and grid[i][j] == grid[i][j+1]:  
        if visited[i][j+1]==0: 
            neighbours.append((i,j+1)) 
        similarNeighbours += 1 
    return neighbours, 4-similarNeighbours

def getAreaSizeAndFencing(startPos, grid, visited): 
    area = 1 
    fences = 0
    neighboursToVisit, newFences = getNeighboursAndNewFences(*startPos, grid, visited)
    fences += newFences
    newlyVisited = visited
    for neighbour in neighboursToVisit: 
        newlyVisited[neighbour[0]][neighbour[1]] = 1
    for neighbour in neighboursToVisit: 
        addedArea, addedFences, newlyVisited = getAreaSizeAndFencing(neighbour, grid, newlyVisited)
        area += addedArea
        fences += addedFences
    return area, fences, newlyVisited

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    nrows, ncols = len(lines), len(lines[0])

    visited = np.zeros((nrows, ncols))

    plantPlots = []
    for i in range(nrows): 
        for j in range(ncols): 
            if visited[i][j]==0: 
                visited[i][j]=1
                area, fences, visited = getAreaSizeAndFencing((i,j), lines, visited)
                plantPlots.append((area, fences))
    
    somme = 0 
    for plantPlot in plantPlots: 
        area, nbFences = plantPlot
        somme += area*nbFences
    return somme
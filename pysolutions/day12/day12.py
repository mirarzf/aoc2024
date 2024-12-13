import numpy as np 

def getNeighboursAndNewFences(i, j, grid, visited): 
    currValue = grid[i][j]
    neighbours = []
    fences = [0,0,0,0]
    if i > 0 and currValue == grid[i-1][j]: 
        if visited[i-1][j]==0: 
            neighbours.append((i-1,j)) 
    else: 
        fences[0] = 1 
    if i < len(grid)-1 and currValue == grid[i+1][j]: 
        if visited[i+1][j]==0: 
            neighbours.append((i+1,j)) 
    else: 
        fences[2] = 1 
    if j > 0 and currValue == grid[i][j-1]:
        if visited[i][j-1]==0: 
            neighbours.append((i,j-1)) 
    else: 
        fences[3] = 1 
    if j < len(grid[0])-1 and currValue == grid[i][j+1]:  
        if visited[i][j+1]==0: 
            neighbours.append((i,j+1)) 
    else: 
        fences[1] = 1 
    return neighbours, fences

def getAreaSizeAndFencing(startPos, grid, visited, sides, areaID = 1): 
    area = 1 
    fences = 0
    neighboursToVisit, fencesPosition = getNeighboursAndNewFences(*startPos, grid, visited)
    newFences = sum(fencesPosition)
    newSides = sides
    if fencesPosition[0]==1: 
        newSides[0][startPos[0], startPos[1]] = 1
    if fencesPosition[1]==1: 
        newSides[1][startPos[0], startPos[1]] = 1
    if fencesPosition[2]==1: 
        newSides[2][startPos[0], startPos[1]] = 1
    if fencesPosition[3]==1: 
        newSides[3][startPos[0], startPos[1]] = 1
    fences += newFences
    newlyVisited = visited
    for neighbour in neighboursToVisit: 
        newlyVisited[neighbour[0]][neighbour[1]] = areaID
    for neighbour in neighboursToVisit: 
        addedArea, addedFences, newlyVisited, newSides = getAreaSizeAndFencing(neighbour, grid, newlyVisited, newSides, areaID)
        area += addedArea
        fences += addedFences
    return area, fences, newlyVisited, newSides

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    nrows, ncols = len(lines), len(lines[0])

    visited = np.zeros((nrows, ncols))
    sides = [np.zeros((nrows, ncols)), np.zeros((nrows, ncols)), np.zeros((nrows, ncols)), np.zeros((nrows, ncols))]
    areaID = 1
    somme = 0
    for i in range(nrows): 
        for j in range(ncols): 
            if visited[i][j]==0: 
                visited[i][j]=areaID
                area, fences, visited, sides = getAreaSizeAndFencing((i,j), lines, visited, sides, areaID)
                if puzzlepart == 1: 
                    somme += area*fences 
                areaID += 1
    
    if puzzlepart == 1: 
        return somme 

    for id in range(1,areaID): 
        plantPlot = np.where(visited == id, 1, 0)
        area = np.sum(plantPlot)

        nbSides = 0 

        plantPlotSide1 = plantPlot*sides[0]
        plantPlotSide2 = plantPlot*sides[2]
        # check all horizontal sides 
        for i in range(nrows): 
            newSides1 = 0 
            newSides2 = 0
            for j in range(ncols-1): 
                if plantPlotSide1[i,j] != plantPlotSide1[i,j+1]: 
                    newSides1 += 1
                if plantPlotSide2[i,j] != plantPlotSide2[i,j+1]: 
                    newSides2 += 1
                    
            nbSides += (newSides1+1)//2 + (newSides2+1)//2
        
        plantPlotSide1 = plantPlot*sides[1]
        plantPlotSide2 = plantPlot*sides[3]
        # check all vertical sides 
        for j in range(ncols): 
            newSides1 = 0 
            newSides2 = 0
            for i in range(nrows-1): 
                if plantPlotSide1[i,j] != plantPlotSide1[i+1,j]: 
                    newSides1 += 1
                if plantPlotSide2[i,j] != plantPlotSide2[i+1,j]: 
                    newSides2 += 1
                    
            nbSides += (newSides1+1)//2 + (newSides2+1)//2
        
        somme += nbSides*area
    return somme 
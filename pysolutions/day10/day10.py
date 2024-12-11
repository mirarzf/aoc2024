import numpy as np 

def getRating(i, j, grid): 
    if grid[i,j]==9: 
        return 1
    else: 
        neighbours = getValidNeighbours((i, j), grid)
        rating = 0
        for neighbour in neighbours: 
            rating += getRating(*neighbour, grid)
        return rating

def getPositionEndOfTrail(i, j, grid): 
    if grid[i,j] == 9: 
        return [(i,j)]
    else: 
        neighbours = getValidNeighbours((i, j), grid)
        finDesChemins = []
        for neighbour in neighbours: 
            finDesChemins += getPositionEndOfTrail(*neighbour, grid)
        return finDesChemins

def getValidNeighbours(position, grid): 
    i, j = position[0], position[1]
    nrows, ncols = grid.shape
    neighbours = []
    if i > 0 and grid[i-1, j]-grid[i,j] == 1: 
        neighbours.append((i-1, j))
    if i < nrows-1 and grid[i+1, j]-grid[i,j] == 1:  
        neighbours.append((i+1, j))
    if j > 0 and grid[i, j-1]-grid[i,j] == 1: 
        neighbours.append((i, j-1))
    if j < ncols - 1 and grid[i, j+1]-grid[i,j] == 1: 
        neighbours.append((i, j+1))
    return neighbours

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    grid = []
    for line in f.readlines(): 
        grid.append([int(e) for e in line.rstrip('\n')])
    f.close()
    grid = np.array(grid)

    somme = 0 
    for i in range(grid.shape[0]): 
        for j in range(grid.shape[1]): 
            if grid[i,j]==0: 
                if puzzlepart == 1: 
                    somme += len(set(getPositionEndOfTrail(i, j, grid)))
                else: 
                    somme += getRating(i, j, grid)

    return somme
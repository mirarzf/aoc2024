import numpy as np 

def moveTop(i, j, grid): 
    posRobot = (i, j)
    k = i-1
    while k > 0 and grid[k, j] == 1: 
        k -= 1
    if k != 0 and grid[k, j] == 0: 
        grid[k, j] = 1
        grid[i-1, j] = 0
        posRobot = (i-1, j)
    return posRobot, grid 

def moveBottom(i, j, grid): 
    posRobot = (i, j)
    k = i+1
    while k < grid.shape[0]-1 and grid[k, j] == 1: 
        k += 1
    if grid[k, j] == 0: 
        grid[k, j] = 1
        grid[i+1, j] = 0
        posRobot = (i+1, j)
    return posRobot, grid 

def moveLeft(i, j, grid): 
    posRobot = (i, j)
    k = j-1
    while k > 0 and grid[i, k] == 1: 
        k -= 1
    if grid[i, k] == 0: 
        grid[i, k] = 1
        grid[i, j-1] = 0
        posRobot = (i, j-1)
    return posRobot, grid 

def moveRight(i, j, grid): 
    posRobot = (i, j)
    k = j+1
    while k < grid.shape[1]-1 and grid[i, k] == 1: 
        k += 1
    if grid[i, k] == 0: 
        grid[i, k] = 1
        grid[i, j+1] = 0
        posRobot = (i, j+1)
    return posRobot, grid 

def sumGPScoordinates(grid): 
    somme = 0 
    for i in range(grid.shape[0]): 
        for j in range(grid.shape[1]): 
            if grid[i,j] == 1: 
                somme += 100*i + j
    return somme 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    
    posGrid = []

    startPos = (0,0)
    i = 0 
    while lines[i] != '': 
        ncols = len(lines[i])
        line = np.zeros(ncols, dtype=int)
        for j in range(ncols): 
            if lines[i][j] == 'O': 
                line[j] = 1 
            elif lines[i][j] == '#': 
                line[j] = 2
            if lines[i][j] == '@': 
                startPos = (i,j)
        posGrid.append(line)
        i += 1
    
    posGrid = np.array(posGrid)

    posRobot = startPos
    for line in lines[i+1:]: 
        for c in line: 
            if c == '^': 
                posRobot, posGrid = moveTop(*posRobot, posGrid)
            elif c == '>': 
                posRobot, posGrid = moveRight(*posRobot, posGrid)
            elif c == 'v': 
                posRobot, posGrid = moveBottom(*posRobot, posGrid)
            elif c == '<': 
                posRobot, posGrid = moveLeft(*posRobot, posGrid)

    return sumGPScoordinates(posGrid)
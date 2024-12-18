import numpy as np 

def getBoxesToMove(i, j, direction, grid, puzzlepart = 1): 
    res = []
    if direction == 'T': 
        if i > 0 and grid[i-1, j] > 1: 
            res.append((grid[i,j],i-1,j))
    if direction == 'R': 
        if j < grid.shape[1]-1 and grid[i, j+1] > 1: 
            res.append((grid[i,j+1],i,j+1))
    return res 

# def moveRight(i, j, grid, boxes): 
#     posRobot = (i, j)
#     k = j+1
#     while k < grid.shape[1]-1 and grid[i, k] > 1: 
#         k += 1
#     if k < grid.shape[1]-1 and grid[i, k] == 0: 
#         boxesLeftToMove = getBoxesToMove(*posRobot, 'R', grid)
#         if len(boxesLeftToMove) > 0: 
#             print(boxesLeftToMove)
#             boxIDtoMove = grid[posRobot]
#             posRobot = i,j+1
#         while len(boxesLeftToMove) > 0: 
#             boxIDtoMove, ki, kj = boxesLeftToMove.pop()
#             boxesLeftToMove += getBoxesToMove(ki, kj, 'R', grid, puzzlepart = 1)
#             # Update the boxes dictionary and the grid 
#             print("inside MoveRight", (ki, kj), boxIDtoMove, grid[ki,kj+1], boxesLeftToMove)
#             grid[ki,kj+1] = boxIDtoMove
#             print(grid[ki, kj+1])
#             if boxIDtoMove > 1: 
#                 boxes[boxIDtoMove] = ((ki,kj+1), boxes[boxIDtoMove][1])
#     grid[posRobot] = 0 
#     return posRobot, grid 


def moveTop(i, j, grid, boxes): 
    posRobot = (i, j)
    k = i-1
    while k > 0 and grid[k, j] > 1: 
        boxes[grid[k,j]] = ((k-1,j), boxes[grid[k,j]][1])
        k -= 1
    if k != 0 and grid[k, j] == 0: 
        grid[k, j] = 2
        grid[i-1, j] = 0
        posRobot = (i-1, j)
    return posRobot, grid 

def moveBottom(i, j, grid, boxes): 
    posRobot = (i, j)
    k = i+1
    while k < grid.shape[0]-1 and grid[k, j] > 1: 
        k += 1
    if grid[k, j] == 0: 
        grid[k, j] = 2
        grid[i+1, j] = 0
        posRobot = (i+1, j)
    return posRobot, grid 

def moveLeft(i, j, grid, boxes): 
    posRobot = (i, j)
    k = j-1
    while k > 0 and grid[i, k] > 1: 
        k -= 1
    if grid[i, k] == 0: 
        grid[i, k] = 2
        grid[i, j-1] = 0
        posRobot = (i, j-1)
    return posRobot, grid 

# def moveRight(i, j, grid, boxes): 
#     posRobot = (i, j)
#     k = j+1
#     while k < grid.shape[1]-1 and grid[i, k] > 1: 
#         k += 1
#     if grid[i, k] == 0: 
#         grid[i, k] = 2
#         grid[i, j+1] = 0
#         posRobot = (i, j+1)
#     return posRobot, grid 

def moveRight(i, j, grid, boxes): 
    posRobot = (i, j)
    k = j+1
    while k < grid.shape[1]-1 and grid[i, k] > 1: 
        k += 1
    if grid[i, k] == 0: 
        grid[i, k] = 2
        grid[i, j+1] = 0
        posRobot = (i, j+1)
        # prevID = grid[i,j]
        # nextID = grid[i,j+1]
        # for kj in range(j+1,k): 
        #     print(prevID, nextID)
        #     nextID = grid[i, kj+1]
        #     grid[i, kj+1] = prevID
        #     prevID = nextID 
    return posRobot, grid 

def sumGPScoordinates(grid): 
    somme = 0 
    for i in range(grid.shape[0]): 
        for j in range(grid.shape[1]): 
            if grid[i,j] > 1: 
                somme += 100*i + j
    return somme 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    
    posGrid = []

    startPos = (0,0)
    i = 0 
    boxID = 2
    boxes = {}
    while lines[i] != '': 
        ncols = len(lines[i])
        line = np.zeros(ncols, dtype=int)
        for j in range(ncols): 
            if lines[i][j] == '#': 
                line[j] = 1 
            elif lines[i][j] == 'O': 
                line[j] = boxID
                boxes[boxID] = (i,j), 'L'
                boxID += 1 
            if lines[i][j] == '@': 
                startPos = (i,j)
        posGrid.append(line)
        i += 1
    
    posGrid = np.array(posGrid)
    posRobot = startPos
    for line in lines[i+1:]: 
        for c in line: 
            if c == '^': 
                posRobot, posGrid = moveTop(*posRobot, posGrid, boxes)
            elif c == '>': 
                posRobot, posGrid = moveRight(*posRobot, posGrid, boxes)
            elif c == 'v': 
                posRobot, posGrid = moveBottom(*posRobot, posGrid, boxes)
            elif c == '<': 
                posRobot, posGrid = moveLeft(*posRobot, posGrid, boxes)
    print(posRobot)
    print(posGrid)

    return sumGPScoordinates(posGrid)
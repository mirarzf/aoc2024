import re 

def getColumn(grid, j): 
    return ''.join(grid[i][j] for i in range(len(grid)))

def getLine(grid, i): 
    return grid[i]

def getNextGuardPosition(grid, dir, i, j): 
    if dir == 'T': 
        signV, signH = -1, 0
    elif dir == 'B': 
        signV, signH = 1, 0 
    if dir == 'L': 
        signV, signH = 0, -1
    elif dir == 'R': 
        signV, signH = 0, 1 

    if dir == 'T' or dir == 'B': 
        column = getColumn(grid, j)
        if dir == 'T': 
            lineInFrontOfGuard = ''.join([column[i-k] for k in range(1,i+1)])
        else: 
            lineInFrontOfGuard = column[i+1:]
    
    else: 
        row = getLine(grid, i)
        if dir == 'L': 
            lineInFrontOfGuard = ''.join(row[j-k] for k in range(1,j+1))
        else: 
            lineInFrontOfGuard = row[j+1:]
    
    indexNextGuardPos = 0 
    while indexNextGuardPos < len(lineInFrontOfGuard) and lineInFrontOfGuard[indexNextGuardPos] != '#': 
        indexNextGuardPos += 1 
    
    return i+signV*indexNextGuardPos, j+signH*indexNextGuardPos

def getNextDir(dir = 'T'): 
    if dir == 'T': 
        return 'R'
    if dir == 'R': 
        return 'B' 
    if dir == 'B': 
        return 'L' 
    if dir == 'L': 
        return 'T'

def isGuardInArea(dir, lastpos, nrows, ncols): 
    if dir == 'T' and lastpos[0] == 0: 
        return False 
    if dir == 'B' and lastpos[0] == nrows-1: 
        return False 
    if dir == 'L' and lastpos[1] == 0: 
        return False 
    if dir == 'R' and lastpos[1] == ncols-1: 
        return False 
    return True 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()] 
    f.close()
    nrows, ncols = len(lines), len(lines[0])

    directions = ['T', 'R', 'B', 'L']

    # Get guard's first position 
    i = 0 
    startPos = -1, -1
    while startPos[0] < 0: 
        if len(re.findall('\^', lines[i])) > 0: 
            matchStartPosition = re.search('\^', lines[i])
            startPos = i, matchStartPosition.span()[0]
        i += 1 
    
    # Initialize list of visited places by guard 
    visited = [startPos]

    # Begin guard searching the area 
    dir = 'T'
    inArea = True 
    while inArea:
        nextGuardPos = getNextGuardPosition(lines, dir, startPos[0], startPos[1])
        
        # Add all visited places by guard 
        smallestI = min(startPos[0], nextGuardPos[0])
        smallestJ = min(startPos[1], nextGuardPos[1])
        iRange, jRange = range(abs(nextGuardPos[0]-startPos[0])+1), range(abs(nextGuardPos[1]-startPos[1])+1)
        for ki in iRange: 
            for kj in jRange: 
                visited.append((smallestI+ki, smallestJ+kj))
        
        # Check if guard is still in the area 
        inArea = isGuardInArea(dir, nextGuardPos, nrows, ncols)

        # Update for next iteration 
        startPos = nextGuardPos
        dir = getNextDir(dir)
    
    return len(set(visited))
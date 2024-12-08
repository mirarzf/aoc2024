import re 

directions = ['T', 'R', 'B', 'L']

def getColumn(grid, j): 
    return ''.join(grid[i][j] for i in range(len(grid)))

def getLine(grid, i): 
    return grid[i]

def getSignVandH(dir = 0): 
    if dir == 0: # Top Direction 
        signV, signH = -1, 0
    elif dir == 1: # Right Direction 
        signV, signH = 0, 1
    elif dir == 2: # Bottom Direction 
        signV, signH = 1, 0 
    else: # dir == 3: # Left Direction 
        signV, signH = 0, -1 
    
    return signV, signH

def getNextToVisit(grid, dir, i, j): 
    signV, signH = getSignVandH(dir)

    if dir % 2 == 0: 
        column = getColumn(grid, j)
        if dir == 0: 
            lineInFrontOfGuard = ''.join([column[i-k] for k in range(i+1)])
        else: 
            lineInFrontOfGuard = column[i:]
    
    else: 
        row = getLine(grid, i)
        if dir == 3: 
            lineInFrontOfGuard = ''.join(row[j-k] for k in range(j+1))
        else: 
            lineInFrontOfGuard = row[j:]
    
    indexNextObsPos = 0
    nextToVisit = []
    while indexNextObsPos < len(lineInFrontOfGuard) and lineInFrontOfGuard[indexNextObsPos] != '#': 
        nextToVisit.append((i+signV*indexNextObsPos, j+signH*indexNextObsPos))
        indexNextObsPos += 1 
    
    # return (i+signV*indexNextObsPos, j+signH*indexNextObsPos), nextToVisit
    return nextToVisit

def isGuardInArea(dir, posBeforeObs, nrows, ncols): 
    if dir == 0 and posBeforeObs[0] == 0: 
        return False 
    if dir == 1 and posBeforeObs[1] == ncols-1: 
        return False 
    if dir == 2 and posBeforeObs[0] == nrows-1: 
        return False 
    if dir == 3 and posBeforeObs[1] == 0: 
        return False 
    return True 

def isThereALoop(visited, pastdirs): 
    lastpos = visited[-1]
    lastdir = pastdirs[-1]

    for i in range(len(visited)-1): 
        if visited[i] == lastpos and pastdirs[i] == lastdir: 
            return True 
    return False 

def guardSearchUntilLoopOrOut(grid, startPos, startDir = 0, keepDirs = False): 
    # Get number max of obstacles 
    nbMaxOfObs = 0 
    for line in grid: 
        nbMaxOfObs += len(re.findall('#', line))
    nbMaxOfObs = 4*nbMaxOfObs
        
    # Begin guard searching the area 
    dir = startDir
    inArea = True 
    noLoop = True 
    visited = [startPos]
    dir_visits = [startDir]
    nbOfObs = 0 
    while inArea and noLoop: 
        nextToVisit = getNextToVisit(grid, dir, startPos[0], startPos[1])
        
        # Add all visited places by guard 
        visited += nextToVisit
        if keepDirs: 
            dir_visits += [dir for i in range(len(nextToVisit))]

        # Check if guard is still in the area 
        inArea = isGuardInArea(dir, visited[-1], len(grid), len(grid[0]))

        if inArea: 
            nbOfObs += 1 
            noLoop = nbOfObs <= nbMaxOfObs 

        # Update for next iteration 
        startPos = visited[-1]
        dir = (dir+1)%4
    
    return visited, dir_visits, noLoop

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()] 
    f.close()
    nrows, ncols = len(lines), len(lines[0])

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
    visited, dir_visits, noLoop = guardSearchUntilLoopOrOut(lines, startPos, 0, keepDirs=(puzzlepart==2))
                
    if puzzlepart == 1: 
        return len(set(visited))
    
    else: 
        # Create list of eligible obstacles 
        eligibleObstacles = []
        for i in range(len(visited)): 
            newStartPos = visited[i]
            # Add obstacles to lines 
            signV, signH = getSignVandH(dir_visits[i])
            obsI, obsJ = newStartPos[0]+signV, newStartPos[1]+signH
            if obsI != -1 and obsI != len(lines) and obsJ != -1 and obsJ != len(lines[0]) and lines[obsI][obsJ] == '.': 
                eligibleObstacles.append((obsI, obsJ))

        eligibleObstacles = set(eligibleObstacles)
        obsCounter = 0 
        for obs in eligibleObstacles: 
            obsI, obsJ = obs[0], obs[1]
            modLines = lines[:obsI]
            newLine = lines[obsI][:obsJ]
            newLine += '#'
            newLine += lines[obsI][obsJ+1:]
            modLines.append(newLine)
            modLines += lines[obsI+1:]
            nextVisited, nextDirs, noLoop = guardSearchUntilLoopOrOut(modLines, startPos, 0)

            if not noLoop: 
                obsCounter += 1

        return obsCounter
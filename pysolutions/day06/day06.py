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
    
    indexNextObsPos = 1
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
    dir = 0
    inArea = True 
    if puzzlepart == 2: 
        dir_visits = [0]
    while inArea:
        nextToVisit = getNextToVisit(lines, dir, startPos[0], startPos[1])
        
        # Add all visited places by guard 
        visited += nextToVisit
        if puzzlepart == 2: 
            dir_visits += [dir for i in range(len(nextToVisit))]

        # Check if guard is still in the area 
        inArea = isGuardInArea(dir, visited[-1], nrows, ncols)

        # Update for next iteration 
        startPos = visited[-1]
        dir = (dir+1)%4
    
            
    if puzzlepart == 1: 
        return len(set(visited))
    
    else: 
        obstaclesList = []
        for i in range(1,len(visited)): 
            dir = dir_visits[i]
            nextDir = dir%4
            nextToVisit = [] 
            while len(nextToVisit) == 0: 
                nextDir = (nextDir+1)%4
                nextToVisit = getNextToVisit(lines, nextDir, visited[i][0], visited[i][1])
            posBeforeObs = nextToVisit[-1]
            if isGuardInArea(nextDir, posBeforeObs, nrows, ncols): 
                j = 0 
                noLoop = True 
                signV, signH = getSignVandH(dir)
                obsToAdd = visited[i][0]+signV, visited[i][1]+signH
                while j < i and noLoop: 
                    if visited[j] == posBeforeObs and dir_visits[j] == nextDir: 
                        obstaclesList.append(obsToAdd)
                        noLoop = False 
                    j+=1 
        print(obstaclesList)
        return len(set(obstaclesList))
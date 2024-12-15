import numpy as np 

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
    
    instructions = []
    for line in lines[i+1:]: 
        instrLine = []
        for j in range(len(line)): 
            if line[j] == '^': 
                instrLine.append(0)
            elif line[j] == '>': 
                instrLine.append(1)
            elif line[j] == 'v': 
                instrLine.append(2)
            elif line[j] == '<': 
                instrLine.append(3)
        instructions.append(instrLine)
    
    print(startPos)

    return 0
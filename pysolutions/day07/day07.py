def formatLine(line): 
    newLine = line.split(' ')
    newLine[0] = newLine[0][:-1]
    return [int(f) for f in newLine]

def isValid(line): 
    if len(line) == 2: 
        if line[0]==line[1]: 
            return True 
        else: 
            return False 

    else: 
        newLinePlus = [line[0]-line[-1]] + line[1:-1]
        newLinePlusValidity = isValid(newLinePlus)
        newLineMul = [line[0]//line[-1]] + line[1:-1]
        newLineMulValidity = isValid(newLineMul)
        return newLinePlusValidity or newLineMulValidity

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')

    sommeOKlines = 0
    for line in f.readlines(): 
        correctLine = formatLine(line.rstrip('\n'))
        if isValid(correctLine): 
            sommeOKlines += correctLine[0]

    f.close()
    return sommeOKlines
def formatLine(line): 
    newLine = line.split(' ')
    newLine[0] = newLine[0][:-1]
    return [int(f) for f in newLine]

def unconcatenateInts(T1, T2): 
    tenPow = len(str(T2))
    return T1//(10**tenPow)

def isValid(line, puzzlepart = 1): 
    if len(line) == 2: 
        if line[0]==line[1]: 
            return True 
        else: 
            return False 

    else: 
        condPuzzle1 = line[0]<line[1] and line[0]%line[1]!=0
        if puzzlepart == 1 and condPuzzle1: 
            return False 
        condPuzzle2 = condPuzzle1 and line[0]%(10**len(str(line[-1])))!=line[-1]
        if puzzlepart == 2 and condPuzzle2: 
            return False 
        newLinePlus = [line[0]-line[-1]] + line[1:-1]
        newLinePlusValidity = isValid(newLinePlus, puzzlepart)
        newLineMul = [line[0]/line[-1]] + line[1:-1]
        newLineMulValidity = isValid(newLineMul, puzzlepart)
        if puzzlepart == 1: 
            return newLinePlusValidity or newLineMulValidity
        else: 
            if line[0]%(10**len(str(line[-1])))==line[-1]: 
                newLineConcat = [unconcatenateInts(line[0],line[-1])] + line[1:-1]
                newLineConcatValidity = isValid(newLineConcat, puzzlepart=puzzlepart)
            else: 
                newLineConcatValidity = False 
            return newLinePlusValidity or newLineMulValidity or newLineConcatValidity

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [formatLine(line.rstrip('\n')) for line in f.readlines()]
    f.close()

    sommeOKlines = 0
    for line in lines: 
        if isValid(line, puzzlepart): 
            sommeOKlines += line[0]

    return sommeOKlines
def getPartNumber(partNbList): 
    n = len(partNbList)
    partNb = 0 
    for i in range(n): 
        partNb += partNbList[i]*10**(n-1-i)
    return partNb

def isPartValid(ncol, partlocs, symbols): 
    for symbol in symbols: 
        i_symbol = symbol[0]//ncol 
        j_symbol = symbol[0]%ncol 
        for partMb in partlocs: 
            i_part = partMb//ncol 
            j_part = partMb%ncol 
            if abs(i_part-i_symbol)<2 and abs(j_part-j_symbol)<2: 
                return True 
    return False 

def getGearRatio(ncol, nrow, schematic, engineParts, symbol): 
    i_symbol = symbol[0]//ncol 
    j_symbol = symbol[0]%ncol 

    validIndices = [] 
    if i_symbol > 0: 
        if j_symbol > 0:
            validIndices.append((i_symbol-1)*ncol+j_symbol-1) 
        validIndices.append((i_symbol-1)*ncol+j_symbol)
        if j_symbol+1 < ncol: 
            validIndices.append((i_symbol-1)*ncol+j_symbol+1)
    if j_symbol > 0: 
        validIndices.append(i_symbol*ncol+j_symbol-1)
    if j_symbol+1 < ncol: 
        validIndices.append(i_symbol*ncol+j_symbol+1)
    if i_symbol+1 < nrow: 
        if j_symbol > 0: 
            validIndices.append((i_symbol+1)*ncol+j_symbol-1)
        validIndices.append((i_symbol+1)*ncol+j_symbol)
        if j_symbol < ncol: 
            validIndices.append((i_symbol+1)*ncol+j_symbol+1)
    adjacentParts = list(set([schematic[index]-2 for index in validIndices if schematic[index]>0]))
    if len(adjacentParts) == 2: 
        firstPart = engineParts[adjacentParts[0]]
        secondPart = engineParts[adjacentParts[1]]
        return getPartNumber(firstPart[0])*getPartNumber(secondPart[0])
    else: 
        return 0 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    sum = 0 

    engineParts = []
    symbols = [] # list of tuples for symbols: (#INDEX, #CHARACTER)
    addNewEnginePart = True 
    schematic = []

    nrow = 0 
    for line in lines: 
        if line != "\n": 
            if nrow == 0: 
                ncol = len(line)-1
            
            for i, e in enumerate(line): 
                if ord(e) > 47 and ord(e) < 58: 
                    if addNewEnginePart: 
                        addNewEnginePart = False 
                        engineParts.append([[int(e)], [i+nrow*ncol]])
                    else: 
                        engineParts[-1][0].append(int(e))
                        engineParts[-1][1].append(i+nrow*ncol)
                    schematic.append(len(engineParts)+1)
                elif e == '.': 
                    if not addNewEnginePart: 
                        addNewEnginePart = True 
                    schematic.append(0)
                elif e == '\n': 
                    if not addNewEnginePart: 
                        addNewEnginePart = True 
                else: # e is a symbol 
                    if not addNewEnginePart: 
                        addNewEnginePart = True 
                    symbols.append( (i+nrow*ncol, e) )
                    schematic.append(1)
                    
            nrow += 1 

    if puzzlepart == 1: 
        for part in engineParts: 
            if isPartValid(ncol, part[1], symbols): 
                sum += getPartNumber(part[0])
    else: # puzzlepart == 2 
        for symbol in symbols: 
            if symbol[1] == '*': 
                sum += getGearRatio(ncol, nrow, schematic, engineParts, symbol)
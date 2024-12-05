import re 

def isCrossMAS(grid, colIndex):     
    concatenatedString = grid[0][colIndex-1] + grid[0][colIndex+1] + grid[2][colIndex-1] + grid[2][colIndex+1]
    if len(re.findall("M", concatenatedString)) == 2 and len(re.findall("S", concatenatedString)) == 2 and len(re.findall(".MM.|.SS.", concatenatedString)) == 0: 
        return True 
    return False 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    grid = [line.rstrip('\n') for line in lines]
    nrows = len(lines)
    ncolumns = len(lines[0].rstrip('\n'))
    compteurXMAS = 0 

    if puzzlepart == 1: 

        for line in lines: 
            # check horizontally 
            compteurXMAS += len(re.findall("XMAS", line))
            # check horizontally backwards 
            compteurXMAS += len(re.findall("SAMX", line))

        for j in range(ncolumns): 
            col = ''.join([line[j] for line in lines])
            # check vertically 
            compteurXMAS += len(re.findall("XMAS", col))
            # check vertically backwards 
            compteurXMAS += len(re.findall("SAMX", col))

        
        for j in range(ncolumns): 
            diagBLtoTR = ''.join([grid[k][j-k] for k in range(min(nrows, j+1))])
            # check diagonally 
            compteurXMAS += len(re.findall("XMAS", diagBLtoTR))
            # check diagonally backwards 
            compteurXMAS += len(re.findall("SAMX", diagBLtoTR))

        for i in range(1, nrows): 
            diagBLtoTR = ''.join([grid[i+k][ncolumns-1-k] for k in range(min(nrows-i,ncolumns))])
            # check diagonally 
            compteurXMAS += len(re.findall("XMAS", diagBLtoTR))
            # check diagonally backwards 
            compteurXMAS += len(re.findall("SAMX", diagBLtoTR))

        for j in range(ncolumns-1, -1, -1): 
            diagTLtoBR = ''.join([grid[k][j+k] for k in range(min(nrows, ncolumns-j))])
            # check diagonally 
            compteurXMAS += len(re.findall("XMAS", diagTLtoBR))
            # check diagonally backwards 
            compteurXMAS += len(re.findall("SAMX", diagTLtoBR))
        
        for i in range(1, nrows): 
            diagTLtoBR = ''.join([grid[i+k][k] for k in range(min(nrows-i, ncolumns))])
            # check diagonally 
            compteurXMAS += len(re.findall("XMAS", diagTLtoBR))
            # check diagonally backwards 
            compteurXMAS += len(re.findall("SAMX", diagTLtoBR))
    
    else: 
        for i in range(1,nrows-1): 
            for j in range(1, ncolumns-1): 
                if grid[i][j] == 'A' and isCrossMAS(grid[i-1:i+2], j): 
                    compteurXMAS += 1       
     
    return compteurXMAS


def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    sum = 0 

    red = 0 
    green = 0 
    blue = 0

    for line in lines: 
        if len(line) > 0: 
            gameID = line[:-1].split(':')[0][5:]
            gameID = int(gameID) 
            gameContent = line.split(':')[1].split(';')
            for match in gameContent: 
                matchContent = match.split(',')
                for marblesSegment in matchContent: 
                    marbles = marblesSegment.split(' ')
                    marblesNb = int(marbles[1])
                    marblesColor = marbles[2].split('\n')[0]
                    if marblesColor == "red" and marblesNb > red: 
                        red = marblesNb 
                    elif marblesColor == "green" and marblesNb > green: 
                        green = marblesNb 
                    elif marblesColor == "blue" and marblesNb > blue: 
                        blue = marblesNb
            
            if puzzlepart == 1 and (red <= 12 and green <= 13 and blue <= 14): 
                sum += gameID 
            if puzzlepart == 2: 
                sum += red * green * blue  
            
            red = 0 
            green = 0 
            blue = 0 

    return sum
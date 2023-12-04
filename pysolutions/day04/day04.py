def checkMatch(winners, mynb): 
    counter = 0 
    for nb in mynb: 
        if nb in winners: 
            counter += 1 
    return counter

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    somme = 0
    nbOfCards = 0
    winpowerlist = []

    for line in lines: 
        winpower = 0 
        if len(line) > 0: 
            nbOfCards += 1 
            line = line[:-1]
            cardID = line.split(':')[0]
            winningNb = [int(nb) for nb in line.split(':')[1].split('|')[0].split()]
            myNb = [int(nb) for nb in line.split(':')[1].split('|')[1].split()]
            winpower = checkMatch(winners=winningNb, mynb=myNb)
            winpowerlist.append(winpower)
    
        if puzzlepart == 1 : 
            if winpower == 0: 
                somme += 0 
            else: 
                somme += 2**(winpower-1)

    nbOfCards = [1]*len(winpowerlist)
    
    if puzzlepart == 2: 
        for i, wp in enumerate(winpowerlist): 
            for j in range(wp): 
                nbOfCards[i+j+1] += nbOfCards[i]
        somme = sum(nbOfCards)

    return somme 
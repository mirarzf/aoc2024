def solve(inputfile : str, puzzlepart : int): 
    f = open(inputfile, 'r')
    lines = f.readlines()

    seedline = lines[0]
    seeds = [int(seed) for seed in seedline.split(':')[1].split()]
    
    mapsList = []
    dest = "seed"
    for line in lines[2:]: 
        if line[0].isalpha(): 
            source = dest
            dest = line.split()[0][len(source)+4:]
            mapsList.append([])
        if line[0].isnumeric(): 
            smallMap = [int(e) for e in line.split()]
            mapsList[-1].append(smallMap)
    
    newseeds = []
    
    for seed in seeds: 
        seedvalue = seed 
        for carte in mapsList: 
            i = 0
            while i < len(carte) and (seedvalue < carte[i][1] or seedvalue > carte[i][1]+carte[i][2]): 
                i += 1
            if i < len(carte): 
                seedvalue = carte[i][0]+(seedvalue-carte[i][1]) 
        newseeds.append(seedvalue)

    return min(newseeds) 
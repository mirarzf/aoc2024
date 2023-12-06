def mapModifier(newRules, currentMapping): 
    newMapping = {}
    for rule in newRules: 
        dest, source, rangeRule = rule[0], rule[1], rule[2]
        for key in currentMapping.keys(): 
            old_dest = currentMapping[key]
            if old_dest >= source and old_dest < source+rangeRule: 
                newvalue = dest + old_dest - source
                newMapping[key] = newvalue
    
    for key in currentMapping.keys(): 
        if key not in newMapping.keys(): 
            newMapping[key] = currentMapping[key]
    
    return newMapping

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

    mapping = {}
    if puzzlepart == 1: 
        for seed in seeds: 
            mapping[seed] = seed

    if puzzlepart == 2: 
        n = len(seeds)//2 
        for i in range(n): 
            seedSource = seeds[2*i]
            for j in range(seeds[2*i+1]): 
                mapping[seedSource+j] = seedSource+j

    for carte in mapsList: 
        mapping = mapModifier(carte, mapping)
    
    return min(mapping.values())
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

def mapModifier2(newRules, oldRules): 
    tempUpdatedRules = oldRules
    toAddRules = []
    for old_rule in tempUpdatedRules: 
        updatedRules = []
        old_dest, old_source, old_range = old_rule[0], old_rule[1], old_rule[2]
        for new_rule in newRules: 
            # print("ahoy", new_rule, tempUpdatedRules, updatedRules)
            new_dest, new_source, new_range = new_rule[0], new_rule[1], new_rule[2]
            
            # CAS 1 : new_rule does not overlap : we do nothing 
            noOverlap = new_source + new_range < old_dest or old_dest + old_range < new_source 
            if noOverlap: 
                updatedRules.append(old_rule)

            # CAS 2 : there is overlap 
            else: # if not noOverlap: 
                range_left = new_source - old_dest 
                range_right = old_dest + old_range - new_source - new_range 
                if range_left > 0: 
                    leftRule = [old_source, old_dest, range_left]
                    updatedRules.append(leftRule)

                    source_middle = old_source+range_left 
                    dest_middle = new_dest 
                else: 
                    source_middle = old_source 
                    dest_middle = new_dest-range_left 
                
                range_middle = min(new_range, old_source+old_range-new_source)
                middleRule = [source_middle, dest_middle, range_middle]
                toAddRules.append(middleRule)
            
                if range_right > 0: 
                    rightRule = [source_middle + range_middle, old_dest, range_right]
                    updatedRules.append(rightRule) 

        tempUpdatedRules = [l for l in updatedRules]

    return updatedRules 

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
    
    if puzzlepart == 1: 
        oldRules = seeds 
    else: 
        oldRules = [] 
        n = len(seeds)//2 
        for i in range(n): 
            seedSource = seeds[2*i]
            oldRules.append([seedSource, seedSource, seeds[2*i+1]])
        for carte in mapsList: 
            oldRules = mapModifier2(carte, oldRules)

    for carte in mapsList: 
        mapping = mapModifier(carte, mapping)
    
    return min(mapping.values())
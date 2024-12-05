def reorderUpdate(successors_dict, update_line): 
    # corrected = [e for e in update_line]
    # for i in range(len(update_line)): 
    #     currPageNb = update_line[i]
    #     currPageNbIndex = i 
    #     nonCorrectedYet = True 
    #     j = i 
    #     while j >= 0 and nonCorrectedYet: 
    #         pred = update_line[j]
    #         if pred in successors_dict[currPageNb]: 
    #             corrected = corrected[:j] + [currPageNb] + corrected[j:currPageNbIndex] + corrected[currPageNbIndex+1:]
    #             nonCorrectedYet = False 
    #         j -= 1 
    # return corrected[len(corrected)//2]
    corrected = [update_line[0]] 
    for i in range(1, len(update_line)): 
        currPageNb = update_line[i]
        addedAfter = []
        if currPageNb in successors_dict.keys(): 
            j = 0 
            while j < len(corrected): 
                pred = corrected[j]
                if pred in successors_dict[currPageNb]: 
                    addedAfter.append(corrected.pop(j))
                else: 
                    j += 1 
        corrected.append(currPageNb)
        corrected += addedAfter
    return corrected[len(corrected)//2]

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()
    
    successors = {}

    i = 0 
    while lines[i].rstrip('\n') != '': 
        ints_from_line = [int(e) for e in lines[i].split('|')]
        if ints_from_line[0] in successors.keys(): 
            successors[ints_from_line[0]].append(ints_from_line[1])
        else: 
            successors[ints_from_line[0]] = [ints_from_line[1]]
        i += 1 
    
    i += 1 
    somme = 0
    while i < len(lines): 
        update_line = [int(e) for e in lines[i].split(',')]
        preds = []
        j = 0 
        updateIsCorrect = True 
        while j < len(update_line) and updateIsCorrect: 
            if update_line[j] in successors.keys(): 
                for invalid_pred in successors[update_line[j]]: 
                    if invalid_pred in preds: 
                        updateIsCorrect = False 
            if updateIsCorrect: 
                preds.append(update_line[j])
                j += 1
        if puzzlepart == 1 and updateIsCorrect: 
            somme += update_line[len(update_line)//2]
        if puzzlepart == 2 and not updateIsCorrect: 
            somme += reorderUpdate(successors, update_line)
        i += 1 
        
    return somme 
def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    line = [int(e) for e in f.read().split(' ')]
    f.close()
    
    # Loop for the number of blinks asked 
    if puzzlepart == 1: 
        totalBlinks = 25 
    else: # puzzlepart == 2 
        totalBlinks = 75 
    for blink in range(totalBlinks): 
        pierresActuelles = {}
        for e in pierresPcdts.keys(): 
            if e == 0: # rule 1 
                if 1 in pierresActuelles.keys(): 
                    pierresActuelles[1] += pierresPcdts[0]
                else: 
                    pierresActuelles[1] = pierresPcdts[0]
            elif len(str(e))%2==0: # rule 2 
                m = len(str(e))//2
                pierre1 = e//(10**m)
                pierre2 = e%(10**m)
                if pierre1 in pierresActuelles.keys(): 
                    pierresActuelles[pierre1] += pierresPcdts[e]
                else: 
                    pierresActuelles[pierre1] = pierresPcdts[e]
                if pierre2 in pierresActuelles.keys(): 
                    pierresActuelles[pierre2] += pierresPcdts[e]
                else: 
                    pierresActuelles[pierre2] = pierresPcdts[e]
            else: # rule 3 
                if 2024*e in pierresActuelles.keys(): 
                    pierresActuelles[2024*e] += pierresPcdts[e]
                else: 
                    pierresActuelles[2024*e] = pierresPcdts[e]
        pierresPcdts = pierresActuelles
    
    for key in pierresActuelles.keys(): 
        somme += pierresActuelles[key]

    return somme
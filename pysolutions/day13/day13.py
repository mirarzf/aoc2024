import numpy as np 

def getkAandkB(ax, ay, bx, by, px, py): 
    kA, kB = 0, 0
    if by*ax-bx*ay != 0: 
        kA = (by*px-bx*py)/(by*ax-bx*ay)
    if ay*bx-ax*by != 0: 
        kB = (ay*px-ax*py)/(ay*bx-ax*by)
    return kA, kB

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    clawMachines = []

    ax, ay, bx, by, px, py = 0, 0, 0, 0, 0, 0
    for line in lines: 
        if line[:8] == 'Button A': 
            inputXandY = line[10:].split(', ')
            ax = int(inputXandY[0][2:])
            ay = int(inputXandY[1][2:])
        if line[:8] == 'Button B': 
            inputXandY = line[10:].split(', ')
            bx = int(inputXandY[0][2:])
            by = int(inputXandY[1][2:])
        if line[:7] == 'Prize: ': 
            inputXandY = line[7:].split(', ')
            if puzzlepart == 1: 
                px = int(inputXandY[0][2:])
                py = int(inputXandY[1][2:])
            else: # puzzlepart == 2 
                px = int(inputXandY[0][2:])+10000000000000
                py = int(inputXandY[1][2:])+10000000000000
            clawMachines.append((ax, ay, bx, by, px, py))
            ax, ay, bx, by, px, py = 0, 0, 0, 0, 0, 0

    
    somme = 0 
    for i in range(len(clawMachines)): 
        kA, kB = getkAandkB(*clawMachines[i])
        ax, ay, bx, by, px, py = clawMachines[i]
        conditionPuzzlepart = (kA <= 100 and kB <= 100) if puzzlepart == 1 else True 
        if np.floor(kA) == kA and np.floor(kB) == kB and kA*ax + kB*bx == px and kA*ay+kB*by==py and conditionPuzzlepart: 
            somme += 3*kA + kB
    somme = int(somme)

    return somme

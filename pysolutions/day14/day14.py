import numpy as np 
import cv2 as cv

def jolieMatrice(matrice, iteration): 
    # filename = f'pysolutions/day14/day14_{iteration}.jpg'
    # cv.imwrite(filename, 255*matrice)
    cv.imshow("Look at that tree!", 255*matrice)
    cv.waitKey(0)

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()
    nrows, ncols = 103, 101
    # nrows, ncols = 7, 11 # TEST VERSION DO NOT FORGET TO COMMENT THIS IF YOU USE THE REAL INPUT 

    initPos = np.zeros((len(lines), 2), dtype=int)
    velocities = np.zeros((len(lines), 2), dtype=int)

    for i, line in enumerate(lines): 
        splittedLine = line.split(' ')
        pos = [int(e) for e in splittedLine[0][2:].split(',')]
        v = [int(e) for e in splittedLine[1][2:].split(',')]
        initPos[i] = np.array([pos[0], pos[1]])
        velocities[i] = np.array([v[0], v[1]])
    
    # Let time pass, 100 seconds 
    finalPos = initPos + 100*velocities
    q1, q2, q3, q4 = 0, 0, 0, 0
    for k in range(len(finalPos)): 
        j, i = finalPos[k][0]%ncols, finalPos[k][1]%nrows

        # check if in Top Left quadrant 
        if i < nrows//2 and j < ncols // 2: 
            q1 += 1        

        # check if in Top Right quadrant 
        if i > nrows//2 and j < ncols // 2: 
            q2 += 1 

        # check if in Bottom Left quadrant 
        if i < nrows//2 and j > ncols // 2: 
            q3 += 1         

        # check if in Bottom Right quadrant 
        if i > nrows//2 and j > ncols // 2: 
            q4 += 1        
    if puzzlepart == 1: 
        return q1*q2*q3*q4
    
    startDisplay = True 
    counter = 7752
    finalPos = initPos+counter*velocities
    while counter < 7753: 
        finalPos[:,0] = (finalPos[:,0]+velocities[:,0]) % ncols
        finalPos[:,1] = (finalPos[:,1]+velocities[:,1]) % nrows
        displayGrid = np.zeros((nrows, ncols), dtype=np.uint8)
        for j,i in finalPos: 
            displayGrid[i, j] = 1
        counter += 1 
        jolieMatrice(displayGrid, counter)
    
    return counter
        

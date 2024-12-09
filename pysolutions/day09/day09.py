def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    line = f.read()
    f.close()
    n = len(line)

    checksum = 0 
    posI = 0 
    lastFileID = n//2 
    j = n-2 if n%2==0 else n-1
    filesNotOrdered = int(line[j])
    i = 0 

    # checkprint = []
    while i < j: 
        # print(i, j, line[i], line[j], len(line))
        fileID = 0 
        blockSizeLeft = int(line[i])
        if i%2 == 0: 
            # on rajoute une valeur qui vient du fond du truc 
            fileID = i//2
            while blockSizeLeft > 0: 
                checksum += posI*fileID
                # checkprint.append(fileID)
                posI += 1 
                blockSizeLeft -= 1 
        else: # i%2 == 1 # on rajoute la valeur du fichier actuel qu'on regarde 
            fileID = lastFileID
            while blockSizeLeft > 0: 
                checksum += posI*fileID 
                # checkprint.append(fileID)
                posI += 1 
                blockSizeLeft -= 1 
                filesNotOrdered -= 1 
                if filesNotOrdered == 0: 
                    j -= 2 
                    filesNotOrdered = int(line[j])
                    lastFileID -= 1 
                    fileID -= 1 
        i += 1 
    while filesNotOrdered > 0: 
        checksum += posI*lastFileID 
        # checkprint.append(fileID)
        posI += 1 
        blockSizeLeft -= 1 
        filesNotOrdered -= 1 
    # print(checkprint)
    return checksum 
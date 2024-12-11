def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    line = f.read()
    f.close()
    n = len(line)

    checksum = 0 

    if puzzlepart == 1: 
        posI = 0 
        lastFileID = n//2 
        j = n-2 if n%2==0 else n-1
        filesNotOrdered = int(line[j])
        i = 0 
        # checkprint = []
        while i < j: 
            fileID = 0 
            blockSizeLeft = int(line[i])
            if i%2 == 0: 
                # on rajoute une valeur qui vient du fond du truc 
                fileID = i//2
                while blockSizeLeft > 0: 
                    checksum += posI*fileID
                    posI += 1 
                    blockSizeLeft -= 1 
            else: # i%2 == 1 # on rajoute la valeur du fichier actuel qu'on regarde 
                fileID = lastFileID
                while blockSizeLeft > 0: 
                    checksum += posI*fileID 
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
            posI += 1 
            blockSizeLeft -= 1 
            filesNotOrdered -= 1 
    
    else: # puzzlepart == 2 
        # Keep a record of the filled spaces that were originally empty 
        actualEmptySizes = []
        lastDiskIndex = 0 
        for i in range(n): 
            if i%2 == 0: 
                actualEmptySizes.append(0)
            else: 
                actualEmptySizes.append(int(line[i]))
            lastDiskIndex += int(line[i])
        if n%2 == 0: 
            lastDiskIndex -= int(line[-1])
        lastDiskIndex -= 1 
        
        # Check backwards the input line and put the last file ID in its best sorted place 
        checksum = 0 
        lineIdx = n-1
        while lineIdx > 0: 
            if lineIdx%2 == 0: 
                fileID = (lineIdx+1)//2 
                filesize = int(line[int(2*fileID)])
                diskIndex = 0 
                noOrderChange = True 
                indexEmptySpace = 0
                while indexEmptySpace < 2*fileID and noOrderChange: 
                    emptySize = actualEmptySizes[indexEmptySpace]
                    if filesize <= emptySize: 
                        diskIndex += int(line[indexEmptySpace])-emptySize
                        for i in range(filesize): 
                            checksum += fileID*diskIndex
                            diskIndex += 1
                        actualEmptySizes[indexEmptySpace] -= filesize
                        noOrderChange = False 
                    else: 
                        diskIndex += int(line[indexEmptySpace])
                    indexEmptySpace += 1
                if noOrderChange: 
                    for i in range(filesize): 
                        checksum += fileID * (lastDiskIndex-i)
            lastDiskIndex -= int(line[lineIdx])
            lineIdx -= 1 
    return checksum 
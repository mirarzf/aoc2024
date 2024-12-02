import numpy as np 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    first_list = []
    second_list = []

    for line in lines: 
        first = int(line.split()[0])
        second = int(line.split()[-1])
        if first != None and second != None:  
            first_list.append(first)
            second_list.append(second)

    first_list.sort()
    second_list.sort()
    first_list = np.array(first_list)
    second_list = np.array(second_list)

    if puzzlepart == 1: 
        return np.sum(np.abs(first_list-second_list))
    else: 
        retval = 0 
        for i in first_list: 
            for j in second_list: 
                if i == j: 
                    retval += i 
        return retval

import re 

def sumOfCorrectMul(line): 
    somme = 0 
    matches = re.findall("mul\([0-9]*,[0-9]*\)", line)
    for m in matches: 
        integers = m[4:-1].split(',')
        somme += int(integers[0])*int(integers[1])
    return somme 


def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    line = f.read()
    f.close()

    somme = 0 

    if puzzlepart == 1: 
        somme += sumOfCorrectMul(line)
    
    else: 
        splittedline = re.split("don't\(\)", line, 1)
        somme += sumOfCorrectMul(splittedline[0])
        
        while len(splittedline) > 1: 
            splittedline = re.split("do\(\)", splittedline[1],1)
            if len(splittedline) > 1: 
                splittedline = re.split("don't\(\)", splittedline[1], 1)
                somme += sumOfCorrectMul(splittedline[0])
    return somme

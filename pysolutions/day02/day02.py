def isReportSafe(report):
    signDiff = -1 
    if len(report) > 0: 
        if report[0] < report[1]: 
            signDiff = +1
    else: 
        return False 
    
    for i in range(len(report)-1): 
        if signDiff*(report[i+1]-report[i]) < 0 or abs(report[i+1]-report[i]) > 3 or report[i+1]==report[i]: 
            return False 
    return True 

def isReportSafeWithModule(report): 
    if isReportSafe(report): 
        return True 
    else: 
        for i in range(len(report)): 
            if isReportSafe(report[:i]+report[i+1:]): 
                return True 
    
    return False 

def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    compteurPart1 = 0 
    compteurPart2 = 0 
    for line in lines: 
        report = [int(e) for e in line.split()]
        if puzzlepart == 1 and isReportSafe(report): 
            compteurPart1 += 1 
        if puzzlepart == 2 and isReportSafeWithModule(report): 
            compteurPart2 += 1 
    return compteurPart1 if puzzlepart == 1 else compteurPart2
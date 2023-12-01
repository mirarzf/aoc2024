def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()

    digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven':7, 'eight':8, 'nine':9}
    digits=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    sumDigits = 0 
    lastDigit = 0
    for line in lines: 
        first = True 
        for i, e in enumerate(line): 
            if ord(e) > 47 and ord(e) < 58: 
                if first: 
                    firstDigit = int(e)
                    first = False 
                lastDigit = int(e)
        
            if puzzlepart == 2: 
                for index, digit in enumerate(digits): 
                    if line[i:i+len(digit)] == digit: 
                        if first: 
                            firstDigit = index+1 
                            first = False 
                        lastDigit = index+1 

        sumDigits += firstDigit*10+lastDigit
    
    return sumDigits
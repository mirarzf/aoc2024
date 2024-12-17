def getBase2(n): 
    bit = []
    a = n 
    while a > 0: 
        r = a%2
        a //= 2 
        bit.append(r)
    return [bit[i] for i in range(len(bit)-1,-1,-1)] 

def getBase10(bit:list): 
    n = len(bit)-1
    a = 0
    for i in range(len(bit)): 
        a += bit[n-i]*(2**i)
    return a

def bitwiseXOR(intA, intB): 
    bitA = getBase2(intA)
    bitB = getBase2(intB)
    bitC = []
    n = min(len(bitA), len(bitB))
    for i in range(n): 
        a = bitA.pop()
        b = bitB.pop()
        if a == b: 
            bitC.append(0)
        else: 
            bitC.append(1)
    while len(bitA) > 0: 
        bitC.append(bitA.pop())
    while len(bitB) > 0: 
        bitC.append(bitB.pop())
    return getBase10([bitC[i] for i in range(len(bitC)-1,-1,-1)])


def doInstruct(opcode, operand, i, A, B, C): 
    newA, newB, newC = A, B, C
    output = []

    # Get the value of the combo operand 
    if operand == 4: 
        combo = A 
    elif operand == 5: 
        combo = B
    elif operand == 6: 
        combo = C
    else: 
        combo = operand

    # Apply instruction depending on opcode  
    if opcode == 0 or opcode == 6 or opcode == 7: 
        res = A // (2**combo)
        if opcode == 0: 
            newA = res 
        elif opcode == 6: 
            newB = res 
        elif opcode == 7: 
            newC = res 
    
    elif opcode == 1: 
        newB = bitwiseXOR(B, operand)
    
    elif opcode == 2: 
        newB = combo%8
    
    elif opcode == 3 and A != 0: 
        return operand, A, B, C, output
    
    elif opcode == 3 and A ==0: 
        return i+2, A, B, C, output
    
    elif opcode == 4: 
        newB = bitwiseXOR(B, C)
    
    else: # opcode == 5: 
        output.append(combo%8)
    
    return i+2, newA, newB, newC, output


def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = [line.rstrip('\n') for line in f.readlines()]
    f.close()

    # Prepare input 
    A = int(lines[0][12:])
    B = int(lines[1][12:])
    C = int(lines[2][12:])
    cmdline = lines[4][9:]
    commandes = [int(cmdline[i]) for i in range(0, len(cmdline), 2)]

    i = 0 
    output = []
    while i < len(commandes): 
        opcode, operand = commandes[i], commandes[i+1]
        i, A, B, C, out = doInstruct(opcode, operand, i, A, B, C)
        if len(out) > 0: 
            output.append(str(out[0]))
    return ','.join(output)
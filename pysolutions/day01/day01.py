def solve(inputfile, puzzlepart): 
    f = open(inputfile, 'r')
    lines = f.readlines()
    f.close()

    first_list = []
    second_list = []

    for line in lines: 
        first, second = line.split(' ')
        first_list.append(first)
        second_list.append(second)

    print(first_list, second_list)

    return 0 
import pysolutions.day01.day01
import pysolutions.day02.day02
import pysolutions.day03.day03
import pysolutions.day04.day04
import pysolutions.day05.day05
import pysolutions.day06.day06
# import pysolutions.day07.day07
# import pysolutions.day08.day08
# import pysolutions.day09.day09
# import pysolutions.day10.day10
# import pysolutions.day11.day11
# import pysolutions.day12.day12
# import pysolutions.day13.day13
# import pysolutions.day14.day14
# import pysolutions.day15.day15
# import pysolutions.day16.day16
# import pysolutions.day17.day17
# import pysolutions.day18.day18
# import pysolutions.day19.day19
# import pysolutions.day20.day20
# import pysolutions.day21.day21
# import pysolutions.day22.day22
# import pysolutions.day23.day23
# import pysolutions.day24.day24
# import pysolutions.day25.day25

class Dailypuzzle: 
    def __init__(self, day, filename) -> None:
        self.day = day
        self.filename = filename 
    
    def solve(self, puzzlepart): 
        daystring = f'day{self.day:02d}'
        subpackage = getattr(pysolutions, daystring)
        module = getattr(subpackage, daystring)
        f = module.solve
        return f(self.filename, puzzlepart)
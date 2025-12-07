from functools import lru_cache
import sys

class Solver:
    def __init__(self, rows):
        self.rows = rows
    
    @lru_cache(maxsize=None)
    def solve(self, ri, ci):
        row = self.rows[ri]
        c = row[ci]
        if c == 'S' or (c == '.' and ri + 1 < len(self.rows)):
            return self.solve(ri + 1, ci)
        elif c == '^':
            return self.solve(ri + 1, ci - 1) + self.solve(ri + 1, ci + 1)
        else:
            return 1

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    solver = Solver([line.strip() for line in lines])
    print(solver.solve(0, lines[0].find('S')))

if __name__ == "__main__":
    main()
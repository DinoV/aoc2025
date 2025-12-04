import sys
from itertools import islice

ZERO = ord('0')
def get_max(bank):
    max = -1
    maxi = 0
    for i, c in enumerate(bank):
        c -= ZERO
        if c > max:
            max = c
            maxi = i
    return max, maxi

DIRS = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)
    
def main():
    with open(sys.argv[1], "r") as f:
        input = f.readlines()

    rows = []
    for row in input:
        row = row.strip()
        rows.append([x for x in row])
        
    changed = True
    removed = 0
    while changed:
        changed = False
        for y, row in enumerate(rows):
            for x, c in enumerate(row):
                if row[x] != '@':
                    continue
                adj = 8
                for xadj, yadj in DIRS:
                    xloc, yloc = x + xadj, y + yadj
                    if xloc >= 0 and yloc >= 0 and xloc < len(row) and yloc < len(rows):
                        val = rows[yloc][xloc]
                        if val == '.':
                            adj -= 1
                    else:
                        adj -= 1
                if adj < 4:
                    removed += 1
                    rows[y][x] = '.'
                    changed = True

    print(removed)



if __name__ == "__main__":
    main()
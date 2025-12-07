import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    rows = []
    for line in lines:
        line = line.strip()
        rows.append([x for x in line])

    splitcnt = 0
    extends = set()
    for ri, row in enumerate(rows):
        for i, c in enumerate(row):
            if c == 'S':
                extends.add(i)
                rows[ri + 1][i] = '|'   
            elif c == '^':
                if rows[ri-1][i]=='|' and ri + 1 < len(rows):
                    split = False
                    if i - 1 not in extends:
                        split = True
                        extends.add(i-1)
                    if i + 1 not in extends:
                        split = True
                        extends.add(i+1)
                    if split:
                        splitcnt += 1
                    rows[ri + 1][i-1] = '|'
                    rows[ri + 1][i+1] = '|'
            elif c == '|':
                if ri + 1 < len(rows) and rows[ri + 1][i] == '.':
                    rows[ri + 1][i] = '|'

        extends = set()
        
    print(splitcnt)

if __name__ == "__main__":
    main()
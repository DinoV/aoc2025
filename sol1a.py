import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    cur = 50
    count = 0
    for line in lines:
        line = line.strip()
        dir = line[0]
        moves = int(line[1:])
        if dir == 'L':
            cur -= moves
        else:
            cur += moves
        cur %= 100
            
        if cur == 0:
            count += 1

    print('password is', count)

if __name__ == "__main__":
    main()
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
        assert moves != 0

        count += moves // 100
        moves = moves % 100

        if dir == 'L':
            if cur and (cur - moves) <= 0:
                count += 1        
            cur -= moves
        else:
            cur += moves
            if cur >= 100:
                count += 1
            
        cur %= 100

    print('password is', count)

if __name__ == "__main__":
    main()
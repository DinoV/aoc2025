import sys

def main():
    with open(sys.argv[1]) as f:
        input = f.readline()

    ranges = input.split(',')
    invalid_total = 0
    for id_set in ranges:
        start, end = id_set.split('-')
        start, end = int(start), int(end)

        for i in range(start, end + 1):
            val = str(i)
            if len(val) % 2 != 0:
                continue
            if val[:len(val)//2] == val[len(val)//2:]:
                invalid_total += i

    print(invalid_total)
    
if __name__ == "__main__":
    main()
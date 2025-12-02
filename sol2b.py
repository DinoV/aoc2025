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
            for divisor in range(2, len(val) + 1):
                if len(val) % divisor != 0:
                    continue
                segment_len = len(val) // divisor
                if val == val[:segment_len] * divisor:
                    invalid_total += i
                    break

    print(invalid_total)
    
if __name__ == "__main__":
    main()
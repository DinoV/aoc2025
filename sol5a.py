import sys
from itertools import islice

def main():
    with open(sys.argv[1], "r") as f:
        input = f.readlines()

    fresh = True
    fresh_ranges = []
    candidates = []
    for row in input:
        row = row.strip()
        if not row:
            fresh = False
            continue

        if fresh:
            start, end = row.split('-')
            fresh_ranges.append((int(start), int(end)))
        else:
            candidates.append(int(row))
            
    available = 0
    for candidate in candidates:
        for start, end in fresh_ranges:
            if candidate >= start and candidate <= end:
                available += 1
                break

    print(available)

if __name__ == "__main__":
    main()
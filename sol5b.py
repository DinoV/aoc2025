import sys
from itertools import islice

def main():
    with open(sys.argv[1], "r") as f:
        input = f.readlines()

    fresh_ranges = []
    for row in input:
        row = row.strip()
        if not row:
            break

        start, end = row.split('-')
        starti, endi = int(start), int(end)
        if not fresh_ranges:
            fresh_ranges.append((starti, endi))
            continue

        for i, (start, end) in enumerate(fresh_ranges):
            if starti <= start:
                #  xxxx
                # nnnnnnn
                if endi >= end:
                    # extend start
                    fresh_ranges[i] = (starti, endi)
                    extend_right(fresh_ranges, starti, endi, i)
                    break
                #   xxxxx
                # nnnnn
                elif endi >= start:
                    fresh_ranges[i] = (starti, end)
                    break
                #      xxxx
                # nnn
                else:
                    fresh_ranges.insert(i, (starti, endi))
                    break
            elif starti >= start and starti <= end:
                #  xxxx
                #   nnnnnnn
                if endi >= end:
                    fresh_ranges[i] = (start, endi)
                    extend_right(fresh_ranges, start, endi, i) 
                #  xxxx
                #   nn
                break
            else:
                assert starti >= start and starti > end and endi > end
        else:
            fresh_ranges.append((starti, endi))


    total = 0
    for start, end in fresh_ranges:
        total += (end - start + 1)
    print(total)

def extend_right(fresh_ranges, start, endi, i):

    while i + 1 < len(fresh_ranges):
        if endi >= fresh_ranges[i + 1][0]:
            fresh_ranges[i] = start, max(endi, fresh_ranges[i + 1][1])
            del fresh_ranges[i + 1]
        else:
            break

if __name__ == "__main__":
    main()
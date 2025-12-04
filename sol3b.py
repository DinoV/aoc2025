import sys
from itertools import islice

ZERO = ord('0')
LEN = 12
def get_min(bank):
    min = 256
    mini = 0
    i = len(bank)
    for c in reversed(bank):
        i -= 1
        c -= ZERO
        if c <= min:
            min = c
            mini = i
        elif min != 256:
            break
    return min, mini

def main():
    with open(sys.argv[1], "rb") as f:
        input = f.readlines()

    total_joltage = 0
    for bank in input:
        bank = bank.strip()

        res = []
        for c in reversed(bank):
            res.append(c)
            if len(res) > LEN:
                min, mini = get_min(res)
                del res[mini]
        joltage = int(''.join(chr(x) for x in reversed(res)))
        total_joltage += joltage

    print(total_joltage)

if __name__ == "__main__":
    main()
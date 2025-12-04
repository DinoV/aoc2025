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

def main():
    with open(sys.argv[1], "rb") as f:
        input = f.readlines()

    total_joltage = 0
    for bank in input:
        bank = bank.strip()

        cur_bank = bank
        max, maxi = get_max(cur_bank)
        if maxi == len(cur_bank) - 1:
            cur_bank = cur_bank[:-1]
            max, maxi = get_max(cur_bank)

        max2, _ = get_max(islice(bank, maxi + 1, None))

        joltage = int(str(max) + str(max2))
        total_joltage += joltage
    print(total_joltage)



if __name__ == "__main__":
    main()
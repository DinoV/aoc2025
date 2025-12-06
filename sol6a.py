import sys
from operator import mul, add

ops = {
    "+": add,
    "*": mul,
}

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    numbers = []
    operators = []
    for line in lines:
        line = line.strip()

        cols = line.split()
        try:
            numbers.append([int(col) for col in cols])
        except:
            operators = [ops[col] for col in cols]

    tots = [1 if op == mul else 0 for op in operators]
    for line in numbers:
        for i, v in enumerate(line):
            tots[i] = operators[i](tots[i], v)
        
    print(sum(tots))

if __name__ == "__main__":
    main()
import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    operators = lines[-1].rstrip('\r\n')
    cur_op = operators[0]
    op_offsets = []
    for i, op in enumerate(operators):
        if i == 0 or op == " ":
            continue
        else:
            assert cur_op == "*" or cur_op == "+"
            op_offsets.append((cur_op, i - 1))
            cur_op = op

    op_offsets.append((cur_op, i + 1))
    
    number_lines = lines[:-1]
    start_offset = 0
    total = 0
    for op, offset in op_offsets:
        tot = 1 if op == "*" else 0
        for i in range(offset - 1, start_offset - 1, -1):
            cur_val = 0
            for line in number_lines:
                if line[i] == ' ':
                    continue
                cur_val = cur_val * 10 + ord(line[i]) - ord('0')

            tot = tot * cur_val if op == "*" else tot + cur_val

        total += tot

        start_offset = offset + 1
    
    print(total)

if __name__ == "__main__":
    main()
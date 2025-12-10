import sys

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    reds = []
    for line in lines:
        line = line.strip()
        line = line.split(",")
        reds.append((int(line[0]), int(line[1])))

    maxi = 0
    maxpts = (-1, -1, -1, -1)
    for i, r1 in enumerate(reds):
        for j, r2 in enumerate(reds):
            if j <= i:
                continue
            x1, y1 = r1
            x2, y2 = r2
            width = abs(x1-x2) + 1
            height = abs(y1-y2) + 1
            if width * height > maxi:
                max = width * height
                maxpts = r1 + r2

    print(maxi, maxpts)

if __name__ == "__main__":
    main()
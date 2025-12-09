import sys

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __hash__(self):
        return self.x ^ self.y ^ self.z
    
    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"
        
def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    points = []
    for line in lines:
        line = line.strip()
        x, y, z = line.split(',')
        points.append(Point(int(x), int(y), int(z)))

    order = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if j <= i:
                continue
            dist = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2
            order.append((dist, p1, p2))

    order.sort(key=lambda k:k[0])
    sets = {}
    set_cnt = 0
    connections = 0
    for dist, p1, p2 in order:
        if p1 in sets and p2 in sets:
            if sets[p1] != sets[p2]:
                set1 = sets[p1]
                set2 = sets[p2]
                # merging two sets
                for p, s in sets.items():
                    if s == set1:
                        sets[p] = set2
        elif p1 in sets:
            sets[p2] = sets[p1]
        elif p2 in sets:
            sets[p1] = sets[p2]
        else:
            set_cnt += 1
            sets[p1] = set_cnt
            sets[p2] = set_cnt
        connections += 1
        if connections == 1000:
            break

    groups = {}
    for k, v in sets.items():
        if v not in groups:
            groups[v] = set()
        g = groups[v]
        g.add(k)

    groups = list(groups.items())
    groups.sort(key = lambda v:len(v[1]), reverse=True)
    print(len(groups[0][1]) * len(groups[1][1]) * len(groups[2][1]))


if __name__ == "__main__":
    main()
from math import e
import sys
from functools import cache
from collections import deque

class Edge:
    def __init__(self, sx, sy, ex, ey):
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey

def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    reds = []
    for line in lines:
        line = line.strip()
        line = line.split(",")
        reds.append((int(line[0]), int(line[1])))

    edges = []
    prev_pt = None
    for pt in reds:
        if prev_pt is not None:
            edges.append(Edge(*prev_pt, *pt))
        prev_pt = pt

    edges.append(Edge(*prev_pt, *reds[0]))
    result = 0
    pts = None
    for i, r1 in enumerate(reds):
        for j, r2 in enumerate(reds):
            x1 = min(r1[0], r2[0])
            x2 = max(r1[0], r2[0])
            y1 = min(r1[1], r2[1])
            y2 = max(r1[1], r2[1])
            if j <= i:
                continue

            width = abs(x1-x2) + 1
            height = abs(y1-y2) + 1

            if width * height < result:
                continue

            intersects = False
            for edge in edges:
                ex1 = min(edge.sx, edge.ex)
                ex2 = max(edge.sx, edge.ex)
                ey1 = min(edge.sy, edge.ey)
                ey2 = max(edge.sy, edge.ey)

                if x1 < ex2 and x2 > ex1 and y1 < ey2 and y2 > ey1:
                    intersects = True
                    break

            if not intersects:
                result = width * height
                pts = r1, r2
    
    print(result, pts)



if __name__ == "__main__":
    main()
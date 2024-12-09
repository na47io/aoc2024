import itertools
from collections import defaultdict
import re


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_bounds(self, r, c):
        return 0 <= self.x < r and 0 <= self.y < c

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if isinstance(other, tuple):
            other = Point(other[0], other[1])

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, tuple):
            other = Point(other[0], other[1])
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __mul__(self, i):
        return Point(self.x * i, self.y * i)

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise IndexError("Index out of range")

    def __eq__(self, other):
        if isinstance(other, tuple):
            other = Point(other[0], other[1])
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def build(fname):
    lines = open(fname, "r").read().splitlines()
    m = defaultdict(list)
    r = len(lines)
    c = len(lines[0])
    expected = set()
    for i in range(r):
        for j in range(c):
            if re.match(r"[a-zA-Z0-9]", lines[i][j]):
                m[lines[i][j]].append(Point(i, j))
            if lines[i][j] == "#":
                expected.add((i, j))

    # order all the points in each key
    for k, v in m.items():
        m[k] = sorted(v)

    return m, r, c, expected


def dist(a, b):
    return a[0] - b[0], a[1] - b[1]


def solve1(fname):
    map, r, c, _ = build(fname)
    pos = set()
    for _, points in map.items():
        for p1, p2 in itertools.combinations(points, 2):
            d = p2 - p1
            if (p := p1 - d) and p.in_bounds(r, c):
                pos.add(p)

            if (p := p2 + d) and p.in_bounds(r, c):
                pos.add(p)

    return len(pos)


def solve2(fname):
    map, r, c, _ = build(fname)
    pos = set()
    for _, points in map.items():
        for p1, p2 in itertools.combinations(points, 2):
            d = p2 - p1

            i = 0
            while True:
                pp1 = p1 - d * i
                pp2 = p2 + d * i
                if not pp1.in_bounds(r, c) and not pp2.in_bounds(r, c):
                    break
                if pp1.in_bounds(r, c):
                    pos.add(pp1)
                if pp2.in_bounds(r, c):
                    pos.add(pp2)
                i += 1

    return len(pos)


if __name__ == "__main__":
    p1_test = solve1("test.txt")
    print("p1 test:", p1_test)
    assert p1_test == 14

    p1 = solve1("input.txt")
    print("p1:", p1)
    assert p1 == 376

    p2_test = solve2("test2.txt")
    print("p2 test:", p2_test)
    assert p2_test == 9

    p2_test = solve2("test.txt")
    print("p2 test:", p2_test)
    assert p2_test == 34

    p2 = solve2("input.txt")
    print("p2:", p2)

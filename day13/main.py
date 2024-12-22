import sys
import functools
from dataclasses import dataclass
import re


@dataclass
class Kek:
    A: tuple[int, int]
    B: tuple[int, int]
    prize: tuple[int, int]


def build(fname):
    lines = open(fname).readlines()
    out = []
    for i in range(0, len(lines), 4):
        _lines = lines[i : i + 3]
        xa, ya = list(map(int, re.findall(r"\d+", _lines[0])))
        xb, yb = list(map(int, re.findall(r"\d+", _lines[1])))
        xp, yp = list(map(int, re.findall(r"\d+", _lines[2])))

        out.append(Kek((xa, ya), (xb, yb), (xp, yp)))

    return out


def solve1(fname):
    machines = build(fname)

    out = 0

    for m in machines:
        xt, yt = m.prize
        print(m)

        @functools.lru_cache
        def _solve(x, y, c, d):
            # if we found the prize return the cost
            if x == xt and y == yt:
                return c

            if d > 99 + 99:
                return 0

            a = _solve(x + m.A[0], y + m.A[1], c + 3, d + 1)
            b = _solve(x + m.B[0], y + m.B[1], c + 1, d + 1)

            if a == 0 and b == 0:
                return 0
            elif a > 0 and b == 0:
                return a
            elif a == 0 and b > 0:
                return b
            else:
                return min(a, b)

        out += _solve(0, 0, 0, 0)

    return out


def solve2(fname):
    machines = build(fname)

    out = 0

    for m in machines:
        xt, yt = m.prize
        xt = xt + 10000000000000
        yt = yt + 10000000000000
        print(m)

        @functools.lru_cache
        def _solve(x, y, c, d):
            # if we found the prize return the cost
            if x == xt and y == yt:
                return c

            if d > 99 + 99:
                return 0

            a = _solve(x + m.A[0], y + m.A[1], c + 3, d + 1)
            b = _solve(x + m.B[0], y + m.B[1], c + 1, d + 1)

            if a == 0 and b == 0:
                return 0
            elif a > 0 and b == 0:
                return a
            elif a == 0 and b > 0:
                return b
            else:
                return min(a, b)

        out += _solve(0, 0, 0, 0)

    return out


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print(t1)
    assert t1 == 480

    p1 = solve1("input.txt")
    print(p1)
    assert p1 == 29598

    p2 = solve2("input.txt")
    print(p2)

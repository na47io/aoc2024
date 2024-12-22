from tqdm import tqdm
import functools
from dataclasses import dataclass
import re


@dataclass
class Kek:
    A: tuple[int, int]
    B: tuple[int, int]
    prize: tuple[int, int]

    def move_prize(self, x, y):
        self.prize = (self.prize[0] + x, self.prize[1] + y)


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
    """
    Smash every button and take the minimum tree.

    This does not scale as the search space increases.

    Relies on bounds for the termination - this is kind of cheating, we should know when we've bottled itkk
    """
    machines = build(fname)

    out = 0

    for m in tqdm(machines):
        xt, yt = m.prize

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


def solve2(fname, offset=0):
    """
    Model as a system of linear equations and solve using Cramer's rule.

    Wikipedia says this blows up in face usually, but i guess we gotta do what sant wants...
    """
    machines = build(fname)

    c = 0

    for m in tqdm(machines):
        m.move_prize(offset, offset)

        # Matrix elements for the system
        a11, a12 = m.A[0], m.B[0]  # x coefficients
        a21, a22 = m.A[1], m.B[1]  # y coefficients
        b1, b2 = m.prize  # target coordinates

        # Calculate determinant
        det = a11 * a22 - a12 * a21

        if det == 0:
            continue

        # Solve the system
        # Using Cramer's rule with extra precision since numbers are large
        a = (b1 * a22 - b2 * a12) / det
        b = (a11 * b2 - a21 * b1) / det

        # Check if we have integer solutions and they're non-negative
        if a != int(a) or b != int(b) or a < 0 or b < 0:
            continue

        # Calculate tokens needed (3 per A press, 1 per B press)
        c += int(3 * a + b)

    return c


if __name__ == "__main__":
    t1 = solve2("test.txt")
    print(t1)
    assert t1 == 480

    p1 = solve2("input.txt")
    print(p1)
    assert p1 == 29598

    p2 = solve2("input.txt", 10000000000000)
    print(p2)
    assert p2 == 93217456941970

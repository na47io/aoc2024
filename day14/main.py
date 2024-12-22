import math
from dataclasses import dataclass
import re


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def build(fname):
    out = []
    for line in open(fname).readlines():
        p, v = line.split(" ")
        x, y = list(map(int, re.findall(r"\d+", p)))
        vx, vy = list(map(int, re.findall(r"-?\d+", v)))

        out.append(Robot(x, y, vx, vy))

    return out


def solve1(fname, h, w):
    robots = build(fname)

    seconds = 100

    mh = h // 2
    mw = w // 2

    print(f"{h=} {w=} {mh=}, {mw=}")

    out = [0, 0, 0, 0]

    for r in robots:
        for _ in range(seconds):
            new_x = (r.x + r.vx) % h
            new_y = (r.y + r.vy) % w
            r.x = new_x
            r.y = new_y

        if r.x < mh and r.y < mw:
            out[0] += 1
        elif r.x > mh and r.y < mw:
            out[1] += 1
        elif r.x < mh and r.y > mw:
            out[2] += 1
        elif r.x > mh and r.y > mw:
            out[3] += 1

    return math.prod(out)


if __name__ == "__main__":
    t1 = solve1("test.txt", 7, 11)
    print(t1)
    assert t1 == 12

    p1 = solve1("input.txt", 101, 103)
    print(p1)

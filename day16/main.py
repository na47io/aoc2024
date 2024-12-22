from heapq import heappush, heappop
import sys


def build(fname):
    map = []
    start = (-1, -1)
    lines = open(fname).readlines()
    for i, line in enumerate(lines):
        row = []
        for j, c in enumerate(line.strip()):
            if c == "S":
                start = (i, j)
            row.append(c)
        map.append(row)

    return map, start


def next_dir(direction, turn):
    if direction == "e":
        if turn == "L":
            return "n"
        elif turn == "R":
            return "s"
    elif direction == "w":
        if turn == "L":
            return "s"
        elif turn == "R":
            return "n"
    elif direction == "n":
        if turn == "L":
            return "w"
        elif turn == "R":
            return "e"
    elif direction == "s":
        if turn == "L":
            return "e"
        elif turn == "R":
            return "w"
    else:
        raise ValueError("Invalid direction")


def solve1(fname):
    map, start = build(fname)
    xs, ys = start

    # Priority queue: (cost, x, y, direction)
    queue = [(0, xs, ys, "e")]
    seen = set()

    while queue:
        cost, x, y, dir = heappop(queue)

        if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]) or map[x][y] == "#":
            continue

        if map[x][y] == "E":
            return cost

        state = (x, y, dir)
        if state in seen:
            continue
        seen.add(state)

        # Go straight
        if dir == "e":
            heappush(queue, (cost + 1, x, y + 1, dir))
        elif dir == "w":
            heappush(queue, (cost + 1, x, y - 1, dir))
        elif dir == "n":
            heappush(queue, (cost + 1, x - 1, y, dir))
        elif dir == "s":
            heappush(queue, (cost + 1, x + 1, y, dir))

        # Turn left/right
        heappush(queue, (cost + 1000, x, y, next_dir(dir, "L")))
        heappush(queue, (cost + 1000, x, y, next_dir(dir, "R")))

    return sys.maxsize


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print(t1)
    assert t1 == 7036

    p1 = solve1("input.txt")
    print(p1)

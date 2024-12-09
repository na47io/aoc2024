class LoopDetected(Exception):
    pass


def build(filename: str):
    lines = open(filename, "r").read().splitlines()

    obstacles = set()
    start = None
    map = []
    for line in lines:
        map.append(list(line))

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "#":
                obstacles.add((i, j))
            if map[i][j] == "^":
                start = (i, j)

    if not start:
        raise Exception("Invalid map. No start found")

    return map, obstacles, start


def walk(map, obstacles, curr, direction):
    visited = set()
    path = set()
    while True:
        if (curr, direction) in path:
            raise LoopDetected
        else:
            path.add((curr, direction))

        visited.add(curr)
        x0, y0 = curr
        x1, y1 = curr  # in case we hit an obstacle

        if direction == "n":
            if (x0 - 1, y0) not in obstacles:
                x1, y1 = (x0 - 1, y0)
            else:
                direction = "e"
        elif direction == "e":
            if (x0, y0 + 1) not in obstacles:
                x1, y1 = (x0, y0 + 1)
            else:
                direction = "s"
        elif direction == "s":
            if (x0 + 1, y0) not in obstacles:
                x1, y1 = (x0 + 1, y0)
            else:
                direction = "w"
        elif direction == "w":
            if (x0, y0 - 1) not in obstacles:
                x1, y1 = (x0, y0 - 1)
            else:
                direction = "n"

        if x1 >= len(map) or y1 >= len(map[0]) or x1 < 0 or y1 < 0:
            break

        curr = x1, y1

    return visited


def solve1(filename):
    map, obstacles, curr = build(filename)
    print(curr)
    visited = walk(map, obstacles, curr, "n")
    return len(visited)


def solve2(filename):
    map, obstacles, curr = build(filename)
    visited = walk(map, obstacles, curr, "n")

    pos = set()
    for point in visited:
        obs = obstacles.copy()
        obs.add(point)

        try:
            _ = walk(map, obs, curr, "n")
        except LoopDetected:
            pos.add(point)

    return len(pos)


if __name__ == "__main__":
    print("part 1:", solve1("input.txt"))
    print("(test) part 2:", solve2("test.txt"))
    part2 = solve2("input.txt")
    print("part 2:", part2)
    assert solve1("input.txt") == 5162
    assert solve2("test.txt") == 6
    assert part2 == 1909
    print("all tests pass.")

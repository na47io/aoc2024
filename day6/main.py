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
            raise ValueError("Loop detected")
        else:
            path.add((curr, direction))

        x, y = curr

        if direction == "n":
            if (x - 1, y) not in obstacles:
                curr = (x - 1, y)
            else:
                direction = "e"
        elif direction == "e":
            if (x, y + 1) not in obstacles:
                curr = (x, y + 1)
            else:
                direction = "s"
        elif direction == "s":
            if (x + 1, y) not in obstacles:
                curr = (x + 1, y)
            else:
                direction = "w"
        elif direction == "w":
            if (x, y - 1) not in obstacles:
                curr = (x, y - 1)
            else:
                direction = "n"

        if x >= len(map) or y >= len(map[0]) or x < 0 or y < 0:
            break

        visited.add(curr)

    return visited


def solve1(filename):
    map, obstacles, curr = build(filename)
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
        except ValueError:
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

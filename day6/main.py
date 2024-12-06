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


def solve1():
    map, obstacles, start = build("input.txt")
    visited = set()
    direction = "n"  # n, e, s, w

    while True:
        x, y = start
        if direction == "n":
            if (x - 1, y) not in obstacles:
                start = (x - 1, y)
            else:
                direction = "e"
        elif direction == "e":
            if (x, y + 1) not in obstacles:
                start = (x, y + 1)
            else:
                direction = "s"
        elif direction == "s":
            if (x + 1, y) not in obstacles:
                start = (x + 1, y)
            else:
                direction = "w"
        elif direction == "w":
            if (x, y - 1) not in obstacles:
                start = (x, y - 1)
            else:
                direction = "n"
        if x >= len(map) or y >= len(map[0]) or x < 0 or y < 0:
            break
        visited.add(start)

    return len(visited)


if __name__ == "__main__":
    print(solve1())

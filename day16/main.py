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


def solve2(fname):
    map, start = build(fname)
    xs, ys = start

    # Track costs to reach each state
    best_costs = {}  # (x, y, dir) -> cost
    best_cost_to_end = sys.maxsize
    all_optimal_tiles = set()

    queue = [(0, xs, ys, "e", [(xs, ys)])]

    while queue:
        cost, x, y, dir, path = heappop(queue)

        # If cost exceeds best path found, skip
        if cost > best_cost_to_end:
            continue

        if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]) or map[x][y] == "#":
            continue

        if map[x][y] == "E":
            if cost <= best_cost_to_end:
                if cost < best_cost_to_end:
                    best_cost_to_end = cost
                    all_optimal_tiles.clear()
                all_optimal_tiles.update(path)
            continue

        state = (x, y, dir)
        # keep walking if the cost at this state is no more than the best path's cost
        if state in best_costs and cost > best_costs[state]:
            continue
        best_costs[state] = cost

        # Go straight
        next_pos = None
        if dir == "e":
            next_pos = (x, y + 1)
        elif dir == "w":
            next_pos = (x, y - 1)
        elif dir == "n":
            next_pos = (x - 1, y)
        elif dir == "s":
            next_pos = (x + 1, y)
        if next_pos:
            heappush(
                queue, (cost + 1, next_pos[0], next_pos[1], dir, path + [next_pos])
            )

        # Turn left/right
        heappush(queue, (cost + 1000, x, y, next_dir(dir, "L"), path))
        heappush(queue, (cost + 1000, x, y, next_dir(dir, "R"), path))

    for i in range(len(map)):
        print(
            "".join(
                [
                    "O" if (i, j) in all_optimal_tiles else map[i][j]
                    for j in range(len(map[0]))
                ]
            )
        )

    return len(all_optimal_tiles)


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print(t1)
    assert t1 == 7036

    p1 = solve1("input.txt")
    print(p1)

    t2 = solve2("test.txt")
    print(t2)
    assert t2 == 45

    p2 = solve2("input.txt")
    print(p2)

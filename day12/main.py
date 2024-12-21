from collections import defaultdict
import uuid


def build(fname):
    map = []
    lines = open(fname).readlines()
    for line in lines:
        map.append([c for c in line.strip()])

    return map


def find_connected_regions(squares):
    if not squares:
        return []

    def get_neighbors(x, y):
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    def flood_fill(start, squares_set, visited):
        stack = [start]
        region = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                region.append(current)

                for neighbor in get_neighbors(*current):
                    if neighbor in squares_set and neighbor not in visited:
                        stack.append(neighbor)

        return region

    squares_set = set(squares)
    visited = set()
    regions = []

    # Continue until we've visited all squares
    while len(visited) < len(squares_set):
        # Find an unvisited square to start a new region
        start = next(square for square in squares if square not in visited)
        region = flood_fill(start, squares_set, visited)
        regions.append(region)

    return regions


def calc_area(coords):
    return len(coords)


def calc_permiter(squares):
    if not squares:
        return 0

    # Initialize each square with perimeter of 4
    total_perimeter = len(squares) * 4

    # Check each pair of squares
    for i, (x1, y1) in enumerate(squares):
        for j, (x2, y2) in enumerate(squares):
            if i != j:
                # If squares share an edge (adjacent), subtract 2 from perimeter
                if (abs(x1 - x2) == 1 and y1 == y2) or (abs(y1 - y2) == 1 and x1 == x2):
                    total_perimeter -= 1

    return total_perimeter


def calc_price(coords):
    total = 0
    for region in find_connected_regions(coords):
        total += calc_area(region) * calc_permiter(region)
    return total


def solve1(fname):
    map = build(fname)

    d = defaultdict(set)

    for i in range(len(map)):
        for j in range(len(map[0])):
            d[map[i][j]].add((i, j))

    return sum([calc_price(coords) for _, coords in d.items()])


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print(t1)
    assert t1 == 772

    p1 = solve1("input.txt")
    print(p1)

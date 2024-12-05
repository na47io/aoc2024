def print_m(m):
    for row in m:
        print("".join(row))


def build_m(filename):
    input = open(filename, "r").read().splitlines()
    m = []
    rows = len(input)
    cols = len(input[0])
    for line in input:
        m.append((["."] * 4) + [c for c in line] + (["."] * 4))

    kek = ["."] * (4 * 2 + cols)

    m = [kek] * 4 + m + [kek] * 4

    print_m(m)
    print(rows, cols)

    return m, rows, cols


def part1(filename):
    m, rows, cols = build_m(filename)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    return sum(
        sum(
            "".join(m[i + di * k][j + dj * k] for k in range(4)) == "XMAS"
            for di, dj in directions
        )
        for i in range(4, rows + 4)
        for j in range(4, cols + 4)
        if m[i][j] == "X"
    )


def part2(filename):
    m, rows, cols = build_m(filename)
    return sum(
        any(t1 + "A" + t2 == "MAS" for t1, t2 in [(x[0], x[2]), (x[2], x[0])])
        and any(t1 + "A" + t2 == "MAS" for t1, t2 in [(y[0], y[2]), (y[2], y[0])])
        for i in range(4, rows + 4)
        for j in range(4, cols + 4)
        if m[i][j] == "A"
        for x, y in [
            (
                (m[i - 1][j - 1], m[i][j], m[i + 1][j + 1]),
                (m[i - 1][j + 1], m[i][j], m[i + 1][j - 1]),
            )
        ]
    )


assert part1("test.txt") == 18
assert part2("test.txt") == 9

print(part2("input.txt"))

import functools


def build(fname):
    map = []

    lines = open(fname).readlines()

    for line in lines:
        map.append([int(c) if c != "." else None for c in line.strip()])

    return map


def solve1(fname):
    map = build(fname)

    @functools.cache
    def _solve(x, y, prev, d):
        """
        How many trails reach this cell.
        """

        if x < 0 or x >= len(map) or y < 0 or y >= len(map[0]):
            # out of bounds
            return []

        curr = map[x][y]

        if curr is None:
            return []

        if d > 9:
            return []

        if prev and curr <= prev:
            return []

        if prev and curr and prev + 1 != curr:
            # not increasing by one
            return []

        if curr == 9 and d == 9:
            # found trail start - return 1
            return [(x, y)]

        return (
            _solve(x + 1, y, curr, d + 1)
            + _solve(x - 1, y, curr, d + 1)
            + _solve(x, y + 1, curr, d + 1)
            + _solve(x, y - 1, curr, d + 1)
        )

    c = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                c += len(set(_solve(i, j, None, 0)))

    return c


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print("t1 answer", t1)
    assert t1 == 36

    p1 = solve1("input.txt")
    print("p1 answer", p1)

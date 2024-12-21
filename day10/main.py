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
        If you can walk to a 9 in 9 incrasing moves, return the coordinates
        """

        # base case
        if (
            (x < 0 or x >= len(map) or y < 0 or y >= len(map[0]))
            or d > 9
            or (curr := map[x][y]) is None
            or (prev is not None and curr and prev + 1 != curr)
        ):
            return set()

        if curr == 9 and d == 9:
            # found trail end, return coords
            return {(x, y)}

        return (
            _solve(x + 1, y, curr, d + 1)
            | _solve(x - 1, y, curr, d + 1)
            | _solve(x, y + 1, curr, d + 1)
            | _solve(x, y - 1, curr, d + 1)
        )

    c = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                res = _solve(i, j, None, 0)
                c += len(res)

    return c


def solve2(fname):
    map = build(fname)

    @functools.cache
    def _solve(x, y, prev, d):
        """
        If you can walk to a 9 in 9 incrasing moves, return the coordinates
        """

        # base case
        if (
            (x < 0 or x >= len(map) or y < 0 or y >= len(map[0]))
            or d > 9
            or (curr := map[x][y]) is None
            or (prev is not None and curr and prev + 1 != curr)
        ):
            return 0

        if curr == 9 and d == 9:
            # found trail end, return coords
            return 1

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
                res = _solve(i, j, None, 0)
                if isinstance(res, set):
                    c += len(res)
                elif isinstance(res, int):
                    c += res
                else:
                    raise ValueError("unexpected type")

    return c


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print("t1 answer", t1)
    assert t1 == 36

    p1 = solve1("input.txt")
    print("p1 answer", p1)
    assert p1 == 816

    p2 = solve2("input.txt")
    print("p2 answer", p2)

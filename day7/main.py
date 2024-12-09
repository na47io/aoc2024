def build(fname):
    lines = open(fname).readlines()
    for line in lines:
        head, t = line.split(":")
        tail = [int(c) for c in t.strip().split(" ")]
        yield (int(head), tail)


def solve1(fname):
    tups = list(build(fname))

    c = 0
    for head, tail in tups:
        n = len(tail)

        def solve(i, c):
            if i == n:
                return c == head

            for i in range(i, n):
                return solve(i + 1, c * tail[i]) or solve(i + 1, c + tail[i])

        if solve(1, tail[0]):
            c += head

    return c


def solve2(fname):
    tups = list(build(fname))

    def concat(a, b):
        """
        Implement || operator that combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.
        """

        a, b = str(a), str(b)
        return int(a + b)

    c = 0
    for head, tail in tups:
        n = len(tail)

        def solve(i, c):
            if i == n:
                return c == head

            for i in range(i, n):
                return (
                    solve(i + 1, c * tail[i])
                    or solve(i + 1, c + tail[i])
                    or solve(i + 1, concat(c, tail[i]))
                )

        if solve(1, tail[0]):
            c += head

    return c


if __name__ == "__main__":
    p1_test = solve1("test.txt")
    print("part1 test:", p1_test)
    p1 = solve1("input.txt")
    print("part1:", p1)

    p2_test = solve2("test.txt")
    print("part2 test:", p2_test)
    p2 = solve2("input.txt")
    print("part2:", p2)

    assert p1_test == 3749
    assert p1 == 8401132154762
    assert p2_test == 11387

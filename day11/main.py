def build(fname):
    out = []
    lines = open(fname).readlines()
    for line in lines:
        out.extend(int(c) for c in line.split(" "))

    return out


def solve1(fname, blinks):
    stones = build(fname)
    c = 0

    while c < blinks:
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif len(strstone := str(s)) % 2 == 0:
                ll = len(strstone) // 2
                new_stones.extend([int(strstone[:ll]), int(strstone[ll:])])
            else:
                new_stones.append(s * 2024)

        stones = new_stones
        c += 1

    return len(stones)


if __name__ == "__main__":
    t1 = solve1("test.txt", 1)
    print(t1)
    assert t1 == 7

    t2 = solve1("test2.txt", 25)
    print(t2)
    assert t2 == 55312

    p1 = solve1("input.txt", 25)
    print(p1)

    p2 = solve1("input.txt", 75)
    print(p2)

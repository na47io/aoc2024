def build(fname):
    with open(fname, "r") as f:
        return f.read().strip()


def solve1(fname):
    line = build(fname)
    s = ""
    i = 0
    id = 0
    for c in line:
        if i % 2 == 0:
            s += str(id) * int(c)
            id += 1
        else:
            s += "." * int(c)
        i += 1

    max_id = id - 1
    i = next(i for i, c in enumerate(s) if c == ".")
    j = len(s)
    while i < j:
        block = s[j - len(str(max_id)) : j]
        block_size = len(block)
        if s[i : i + block_size] == "." * block_size:
            s = s[:i] + block + s[i + block_size :]
            s = s[: j - len(str(max_id))] + "." * (block_size + len(s[j:]))
            while s[i] != ".":
                i += 1
            j -= block_size
        print(s)

    return 0


if __name__ == "__main__":
    p1_test = solve1("test.txt")
    print("p1 test:", p1_test)
    assert p1_test == 1928

    # p1 = solve1("input.txt")
    # print("p1:", p1)

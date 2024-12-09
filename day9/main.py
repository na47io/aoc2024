def build(fname):
    with open(fname, "r") as f:
        return f.read().strip()


def solve1(fname):
    diskmap = build(fname)
    s = ""
    i = 0
    id = 0
    for c in diskmap:
        # even position in map means store c blocks at current id
        if i % 2 == 0:
            s += str(id) * int(c)
            id += 1
        # odd position means c blank blocks
        else:
            s += "." * int(c)
        i += 1

    idr = id - 1
    idl = 0  # left id, can infer right id from block size
    print(s, "max_id", idr)
    i = 0
    j = len(s)
    c = 0
    while i < j:
        block = s[j - len(str(idr)) : j]  # get last len(idr) chars
        block_size = len(block)

        # move right pointer if cant grab a block
        if "." in block:
            j -= 1
            continue

        # move left pointer until block fits into space
        if s[i : i + block_size] != "." * block_size:
            while s[i] != ".":
                checksum = int(i) * idl
                print(f"{i} * {idl}={checksum}")
                c += checksum
                i += 1
            idl += 1
            continue

        # copy right block into space on the left
        s = s[:i] + block + s[i + block_size :]
        s = s[: j - len(str(idr))] + "." * (block_size + len(s[j:]))
        print(s, block_size, i, j)

        # add copied block to the checksum
        checksum = int(i) * int(block)
        print(f"{i} * {block}={checksum}")
        c += checksum
        i += block_size
        j -= block_size

    assert s == "0099811188827773336446555566................."

    return c


if __name__ == "__main__":
    p1_test = solve1("test.txt")
    print("p1 test:", p1_test)
    assert p1_test == 1928

    # p1 = solve1("input.txt")
    # print("p1:", p1)

def build(fname):
    with open(fname, "r") as f:
        return f.read().strip()


def from_map(diskmap: str):
    # Pre-calculate filled positions during initial setup
    filled = []  # List of (position, id) pairs
    empty = []  # Just positions

    pos = 0
    id = 0
    for i, c in enumerate(diskmap):
        count = int(c)
        if i % 2 == 0:
            for _ in range(count):
                filled.append((pos, id))
                pos += 1
            id += 1
        else:
            for _ in range(count):
                empty.append(pos)
                pos += 1

    filled.sort(reverse=True)  # Sort by position descending
    return filled, empty, pos  # pos is total length


def solve1(fname):
    diskmap = build(fname)
    filled, empty, total_len = from_map(diskmap)

    # Initialize result array
    result = [None] * total_len
    for pos, id in filled:
        result[pos] = id

    empty_idx = 0  # Index into empty list
    # Process each filled position from right to left
    for _, (pos, id) in enumerate(filled):
        # If there's an empty spot to the left and we're not at leftmost
        if empty_idx < len(empty) and empty[empty_idx] < pos:
            # Move to empty spot
            result[empty[empty_idx]] = id
            result[pos] = None
            empty_idx += 1

    return sum(i * id for i, id in enumerate(result) if id is not None)


if __name__ == "__main__":
    p1_test = solve1("test.txt")
    print("p1 test:", p1_test)
    assert p1_test == 1928

    import time

    t = time.time()
    p1 = solve1("input.txt")
    print("time:", time.time() - t)
    print("p1:", p1)
    assert p1 == 6334655979668

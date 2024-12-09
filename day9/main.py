def build(fname):
    with open(fname, "r") as f:
        return f.read().strip()


def from_map(diskmap: str):
    slots = []
    i = 0
    id = 0
    for c in diskmap:
        if i % 2 == 0:  # File blocks
            for _ in range(int(c)):
                slots.append(id)
            id += 1
        else:  # Empty blocks
            slots.extend([None] * int(c))
        i += 1
    return slots


def solve1(fname):
    diskmap = build(fname)
    slots = from_map(diskmap)

    # Keep going until we can't find any moves to make
    while True:
        # Find rightmost filled slot
        right_pos = -1
        for i in range(len(slots) - 1, -1, -1):
            if slots[i] is not None:
                right_pos = i
                break
        if right_pos == -1:
            break

        # Find leftmost empty slot before right_pos
        left_pos = -1
        for i in range(right_pos):
            if slots[i] is None:
                left_pos = i
                break

        # If no empty slots found, we're done
        if left_pos == -1:
            break

        # Move the value left
        slots[left_pos] = slots[right_pos]
        slots[right_pos] = None

    # Calculate checksum
    return sum(i * id for i, id in enumerate(slots) if id is not None)


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

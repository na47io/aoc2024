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


def solve2(fname, debug=False):
    diskmap = build(fname)

    # Build files info: [(start_pos, size, id), ...]
    files = []
    pos = 0
    id = 0

    for i, c in enumerate(diskmap):
        count = int(c)
        if i % 2 == 0:
            files.append((pos, count, id))
            pos += count
            id += 1
        else:
            pos += count

    # Build gaps info: [(start_pos, size), ...]
    gaps = []
    pos = 0
    for i, c in enumerate(diskmap):
        count = int(c)
        if i % 2 == 1 and count > 0:  # Only add non-zero gaps
            gaps.append((pos, count))
        pos += count

    # Process files in reverse ID order
    files.sort(key=lambda x: x[2], reverse=True)  # Sort by ID descending
    result = [None] * pos  # Initialize result array

    # Place all files in their original positions first
    for start, size, id in files:
        for i in range(size):
            result[start + i] = id

    # Try to move each file left
    for file_start, file_size, file_id in files:
        # Find leftmost gap that can fit this file
        best_gap = None
        for gap_start, gap_size in gaps:
            if gap_start < file_start and gap_size >= file_size:
                best_gap = gap_start
                break

        if best_gap is not None:
            # Clear old position
            for i in range(file_size):
                result[file_start + i] = None
            # Move to new position
            for i in range(file_size):
                result[best_gap + i] = file_id
            # Update gaps
            gaps = [(s, sz) for s, sz in gaps if s != best_gap]
            if gap_size > file_size:
                gaps.append((best_gap + file_size, gap_size - file_size))
            gaps.append((file_start, file_size))
            gaps.sort()  # Keep gaps sorted

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

    p2_test = solve2("test.txt")
    print("p2 test:", p2_test)
    assert p2_test == 2858

    t = time.time()
    p2 = solve2("input.txt")
    print("time:", time.time() - t)
    print("p2:", p2)

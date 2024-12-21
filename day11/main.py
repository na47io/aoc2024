def build(fname):
    out = []
    lines = open(fname).readlines()
    for line in lines:
        out.extend(int(c) for c in line.split(" "))

    return out


def solve(fname, blinks):
    # Map of number -> count of occurrences
    counts = {}
    for n in build(fname):
        counts[n] = counts.get(n, 0) + 1

    for _ in range(blinks):
        new_counts = {}
        for num, freq in counts.items():
            if num == 0:
                new_counts[1] = new_counts.get(1, 0) + freq
            else:
                s = str(num)
                if len(s) % 2 == 0:
                    # Split numbers in half
                    mid = len(s) // 2
                    left = int(s[:mid])
                    right = int(s[mid:])
                    new_counts[left] = new_counts.get(left, 0) + freq
                    new_counts[right] = new_counts.get(right, 0) + freq
                else:
                    # Multiply by 2024
                    new_val = num * 2024
                    new_counts[new_val] = new_counts.get(new_val, 0) + freq
        counts = new_counts

    return sum(counts.values())


if __name__ == "__main__":
    t1 = solve("test.txt", 1)
    print(t1)
    assert t1 == 7

    t2 = solve("test2.txt", 25)
    print(t2)
    assert t2 == 55312

    p1 = solve("input.txt", 25)
    print(p1)
    assert p1 == 194482

    p2 = solve("input.txt", 75)
    print(p2)

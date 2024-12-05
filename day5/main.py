from collections import defaultdict
from functools import cmp_to_key


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)

    def append(self, nodestr):
        n1, n2 = nodestr.split("|")
        self.nodes.add(int(n1))
        self.nodes.add(int(n2))
        self.edges[int(n1)].append(int(n2))

    def check_path(self, path: list[int]) -> bool:
        for i in range(1, len(path)):
            if path[i] not in self.edges[path[i - 1]]:
                return False
        return True

    def __str__(self):
        return str(self.edges)


def build(filename):
    input = open(filename, "r").read().splitlines()
    g = Graph()
    updates = []
    pointer = g
    for line in input:
        if not line:
            pointer = updates
            continue
        pointer.append(line)

    updates = [[int(x) for x in update.split(",")] for update in updates]

    return g, updates


def part1(filename):
    g, updates = build(filename)
    count = 0

    for update in updates:
        if g.check_path(update):
            count += update[len(update) // 2]

    return count


def part2(filename):
    g, updates = build(filename)
    count = 0

    def cmp(n2, n1):
        print(f"checking...{n1} -> {n2} ", end="")
        if n2 in g.edges[n1]:
            print("found edge, do nothing")
            # if there is an edge from n1 to n2, n2 should come before n1, reorder
            return 0

        print(f"no edge found, {n2} comes before {n1}")
        # if there is no edge,
        return -1

    for update in updates:
        if not g.check_path(update):
            print(update)
            fixed_update = sorted(update, key=cmp_to_key(cmp))
            print(fixed_update)
            count += fixed_update[len(fixed_update) // 2]

    return count


assert part1("test.txt") == 143
print(part1("input.txt"))

assert part2("test.txt") == 123
# print(part2("input.txt"))

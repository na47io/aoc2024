def build(fname):
    with open(fname, "r") as f:
        return f.read().strip()


class Block:
    def __init__(self, is_empty=False, size=None, id=None):
        self.is_empty = is_empty
        self.size = size
        self.id = id

    @staticmethod
    def empty(size):
        return Block(is_empty=True, id=None, size=size)

    @staticmethod
    def data(id):
        return Block(is_empty=False, id=id, size=len(str(id)))

    def __str__(self):
        if self.is_empty and self.size is not None:
            return "." * self.size
        if self.id is None:
            print(self.is_empty, self.size, self.id)
            raise Exception("WTDDD")
        return str(self.id)


class Disk:
    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        self.blocks.append(block)

    @staticmethod
    def from_map(diskmap: str):
        i = 0
        id = 0
        disk = Disk()
        for c in diskmap:
            # even position in map means store c blocks at current id
            if i % 2 == 0:
                for _ in range(int(c)):
                    disk.add_block(Block.data(id))
                id += 1
            # odd position means c blank blocks
            else:
                size = int(c)
                if size:
                    disk.add_block(Block.empty(size=size))
            i += 1

        return disk

    def __str__(self):
        return "".join([str(b) for b in self.blocks])

    def __repr__(self):
        return self.__str__()

    def peek(self):
        for i in range(len(self.blocks) - 1, -1, -1):
            if not self.blocks[i].is_empty:
                return self.blocks[i], i

        return None, -1

    def is_compact(self):
        _, ix = self.peek()
        for i in range(len(self.blocks)):
            if i <= ix and self.blocks[i].is_empty:
                return False
            if i > ix and not self.blocks[i].is_empty:
                return False
        return True

    def pop(self):
        # remove the last non-empty block
        for i in range(len(self.blocks) - 1, -1, -1):
            if not self.blocks[i].is_empty:
                el = self.blocks.pop(i)
                self.blocks.insert(i, Block.empty(el.size))
                return el

    def insert(self, block):
        """
        Find an empty block whose size is greater or equal to this block id and insert it
        """
        for i, b in enumerate(self.blocks):
            if b.is_empty and b.size == block.size:
                # replace the empty block with the new block
                _ = self.blocks.pop(i)
                self.blocks.insert(i, block)
                return
            elif b.is_empty and b.size > block.size:
                # split the empty block into two
                self.blocks.pop(i)
                self.blocks.insert(i, Block.empty(b.size - block.size))
                self.blocks.insert(i, block)
                return
            else:
                continue

    def checksum(self):
        return sum(b.id * i for i, b in enumerate(self.blocks) if not b.is_empty)


def solve1(fname, debug=False):
    diskmap = build(fname)
    disk = Disk.from_map(diskmap)

    if debug:
        assert str(disk) == "00...111...2...333.44.5555.6666.777.888899"

    print("compressing...")
    while not disk.is_compact():
        last = disk.pop()
        disk.insert(last)
    print("finished")

    if debug:
        assert str(disk) == "0099811188827773336446555566.............."

    return disk.checksum()


if __name__ == "__main__":
    p1_test = solve1("test.txt", debug=True)
    print("p1 test:", p1_test)
    assert p1_test == 1928

    # p1 = solve1("input.txt")
    # print("p1:", p1)

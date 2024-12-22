import re
from tqdm import tqdm


def xor(a, b):
    """
    Bitwise xor of two numbers
    """
    return a ^ b


class Computer:
    a: int
    b: int
    c: int

    program: list[int]
    n: int

    def __init__(self, program: list[int]):
        self.program = program
        self.n = len(program)

    def init(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.out = []
        self.nout = 0
        self.ip = 0

    def step(self, ip, debug=False):
        if self.a is None or self.b is None or self.c is None:
            raise ValueError("call init(a,b,c) with initial values")

        self.ip = ip

        try:
            (opcode, operand) = self.program[self.ip], self.program[self.ip + 1]
        except IndexError:
            return
        if debug:
            print(f"{opcode=}, {operand=} {self.a=} {self.b=} {self.c=} {self.ip=}")
        if opcode == 0:
            self.a = self.a >> self._load_operand(operand)
        elif opcode == 1:
            self.b = xor(self.b, operand)
        elif opcode == 2:
            self.b = self._load_operand(operand) & 7
        elif opcode == 3:
            if self.a != 0:
                return operand
        elif opcode == 4:
            self.b = xor(self.b, self.c)
        elif opcode == 5:
            x = self._load_operand(operand) & 7
            self.out.append(x)
            self.nout += 1
        elif opcode == 6:
            self.b = self.a >> self._load_operand(operand)
        elif opcode == 7:
            self.c = self.a >> self._load_operand(operand)
        else:
            raise ValueError(f"Invalid opcode {opcode}")

        nxt = self.ip + 2
        if nxt < self.n:
            return nxt

        return -1

    def output(self):
        return ",".join(map(str, self.out))

    def _load_operand(self, operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        elif operand == 7:
            raise ValueError("Reserved operand 7")
        else:
            raise ValueError(f"Invalid operand {operand}")


def build(fname):
    lines = open(fname).readlines()

    a = next(map(int, re.findall(r"\d+", lines[0])))
    b = next(map(int, re.findall(r"\d+", lines[1])))
    c = next(map(int, re.findall(r"\d+", lines[2])))

    program = [int(c) for c in lines[4].split(":")[1].strip().split(",")]
    return Computer(program), a, b, c


def solve1(fname):
    computer, a, b, c = build(fname)

    computer.init(a, b, c)
    ip = 0

    while True:
        ip = computer.step(ip)
        if ip == -1:
            break

    return computer.output()


def solve2(fname):
    """
    Brute force by trying hella numbers...
    """
    computer, _, b, c = build(fname)

    for a in range(2**64):
        computer.init(a, b, c)
        ip = 0

        while True:
            ip = computer.step(ip)

            if any(x != y for x, y in zip(computer.program, computer.out)):
                break

            if ip == -1:
                break

            if computer.nout == computer.n:
                return a

    return -1


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print(t1)
    assert t1 == "4,6,3,5,6,3,5,2,1,0"

    p1 = solve1("input.txt")
    print(p1)
    assert p1 == "7,1,3,7,5,1,0,3,4"

    t2 = solve2("test2.txt")
    print(t2)
    assert t2 == 117440

    p2 = solve2("input.txt")
    print(p2)

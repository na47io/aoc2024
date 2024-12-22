import re


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

    def __init__(self, a: int, b: int, c: int, program: list[int]):
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.out = []
        self.ip = 0

    def run(self, debug=False):
        while self.ip < len(self.program):
            try:
                (opcode, operand) = self.program[self.ip], self.program[self.ip + 1]
            except IndexError:
                return
            if debug:
                print(f"{opcode=}, {operand=} {self.a=} {self.b=} {self.c=} {self.ip=}")
            if opcode == 0:
                self.a = self.a // 2 ** self._load_operand(operand)
            elif opcode == 1:
                self.b = xor(self.b, self._load_literal_operand(operand))
            elif opcode == 2:
                self.b = self._load_operand(operand) % 8
            elif opcode == 3:
                if self.a != 0:
                    self.ip = self._load_literal_operand(operand)
                    continue
            elif opcode == 4:
                self.b = xor(self.b, self.c)
            elif opcode == 5:
                x = self._load_operand(operand) % 8
                self.out.append(x)
            elif opcode == 6:
                self.b = self.a // 2 ** self._load_operand(operand)
            elif opcode == 7:
                self.c = self.a // 2 ** self._load_operand(operand)
            else:
                raise ValueError(f"Invalid opcode {opcode}")

            self.ip += 2

    def _load_literal_operand(self, operand):
        if operand <= 7:
            return operand
        else:
            raise ValueError(f"Not a literal operand {operand}")

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
    print(a, b, c, program)
    return Computer(a, b, c, program)


def solve1(fname):
    computer = build(fname)

    computer.run()

    return ",".join(map(str, computer.out))


if __name__ == "__main__":
    t1 = solve1("test.txt")
    print(t1)
    assert t1 == "4,6,3,5,6,3,5,2,1,0"

    p1 = solve1("input.txt")
    print(p1)

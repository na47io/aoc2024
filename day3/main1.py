import re

input = open("input.txt", "r").read()

regex = r"mul\((\d+),(\d+)\)"

g = re.findall(regex, input, re.MULTILINE)

print(g)

c = 0
for x, y in g:
    c += int(x) * int(y)

print(c)

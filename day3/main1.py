import re

input = open("input.txt", "r").read()

regex = "(do)\(\)|(don't)\(\)|mul\((\d+),(\d+)\)"

g = re.findall(regex, input, re.MULTILINE)

print(g)

c = 0
on = True
for do, dont, x, y in g:
    if dont:
        on = False
    if do:
        on = True
    if x and y:
        c += int(x) * int(y) if on else 0

print(c)

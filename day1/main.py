lines = open('input.txt', 'r').read().splitlines()

print('total lines', len(lines))

l1, l2 = [], []

for l in lines:
    x, y = [int(x) for x in l.split(' ') if x]
    l1.append(x)
    l2.append(y)

l1 = sorted(l1)
l2 = sorted(l2)

ans = sum(abs(x-y) for x, y in zip(l1, l2))
    


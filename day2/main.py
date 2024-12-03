# 625 is TOO HIGH
# 577 is TOO HIGH

reports = open("inputs.txt").read().splitlines()

c = 0
for report in reports:
    report = [int(x) for x in report.split(" ")]

    sign = None
    prev = None
    badc = 0
    for i in range(len(report)):
        if i == 0:
            prev = report[i]
            continue

        d = report[i] - prev

        if not sign:
            sign = 1 if d >= 0 else -1

        if d * sign <= 0 or abs(d) > 3:
            break

        prev = report[i]

        if i == len(report) - 1:
            c += 1

assert c == 559
print("test passed")

"""
Solve 2.1 without allocating a new list for every permutation
"""

reports = open("inputs.txt").read().splitlines()


def is_report_safe(report):
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

        prev = report[i]

        if d * sign <= 0 or abs(d) > 3:
            if badc == 0:
                badc = 1
                continue
            else:
                break

        if i == len(report) - 1:
            return True

    return False


c = 0
for report in reports:
    if is_report_safe(report):
        c += 1

print(c)
assert c == 559
print("test passed")

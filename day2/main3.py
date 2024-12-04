"""
Solve 2.1 without allocating a new list for every permutation
"""

reports = open("inputs2.txt").read().splitlines()


def is_report_safe(report, debug=False):
    report = [int(x) for x in report.split(" ")]

    sign = None
    prev = report[0]
    badc = 0
    i = 1
    while i < len(report):
        d = report[i] - prev

        if not sign:
            sign = 1 if d >= 0 else -1

        if debug:
            print(i)
            if d * sign <= 0 or abs(d) > 3:
                print(prev, report[i], "is bad")
            else:
                print(prev, report[i], "is good")

        if d * sign <= 0 or abs(d) > 3:
            if badc == 0:
                badc = 1
                # i += 2
                # report[i] = prev
                # i += 1
                # continue
            else:
                break

        prev = report[i]

        if i == len(report) - 1:
            return True

        i += 1

    return False


def solve():
    reports = open("inputs.txt").read().splitlines()
    c = 0
    for report in reports:
        if is_report_safe(report):
            c += 1
    return c


def dev(sreport):
    print(sreport)
    assert is_report_safe(sreport, debug=True)


def test():
    reports = open("inputs2.txt").read().splitlines()
    c = 0
    for report in reports:
        if is_report_safe(report):
            c += 1
        else:
            print(report)


# assert solve() == 559
# test()
dev("67 65 68 71 72 73 74")
dev("3 6 8 10 13 14 11 15")

# 625 is TOO HIGH
# 577 is TOO HIGH

reports = open("inputs.txt").read().splitlines()

c = 0
for report in reports:
    report = [int(x) for x in report.split(" ")]
    sign = None
    for i in range(1, len(report)):
        d = report[i] - report[i - 1]
        if d == 0:
            break
        if not sign:
            sign = "inc" if d > 0 else "dec"
        else:
            if sign == "inc" and d < 0:
                break
            if sign == "dec" and d > 0:
                break

        if abs(d) > 3:
            break

        if i == len(report) - 1:
            c += 1

assert c == 559
print("test passed")

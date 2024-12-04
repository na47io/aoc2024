reports = open("inputs.txt").read().splitlines()


def is_report_safe(report):
    sign = None
    prev = None
    for i in range(len(report)):
        if i == 0:
            prev = report[i]
            continue

        d = report[i] - prev

        if not sign:
            sign = 1 if d >= 0 else -1

        prev = report[i]

        if d * sign <= 0 or abs(d) > 3:
            break

        if i == len(report) - 1:
            return True

    return False


def permute_reports(report):
    for i in range(len(report)):
        yield report[:i] + report[i + 1 :]


c = 0
with open("inputs2.txt", "w") as f:
    for sreport in reports:
        report = [int(x) for x in sreport.split(" ")]
        permted_reports = permute_reports(report)
        for r in permted_reports:
            if is_report_safe(r):
                c += 1
                f.write(report + "\n")
                break

print(c)
assert c == 601
print("test passed")

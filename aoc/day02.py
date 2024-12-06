from aoc.const import INPUT_ROOT


def is_safe(report: list[int], min_step_size: int = 1, max_step_size: int = 3) -> bool:
    is_asc: bool = report[0] < report[1]
    report_size = len(report)
    for i, lvl in enumerate(report):
        if i == report_size - 1:
            break

        step_size = lvl - report[i + 1]
        if is_asc and step_size > 0:
            return False

        if not is_asc and step_size < 0:
            return False

        if not (min_step_size <= abs(step_size) <= max_step_size):
            return False

    return True


def part1(reports: list[list[int]]) -> int:
    total = 0
    for report in reports:
        if not is_safe(report):
            continue

        total += 1

    return total


def part2(reports) -> int:
    total = 0
    for report in reports:
        results = []
        for i in range(len(report)):
            tmp_report = report.copy()
            tmp_report.pop(i)

            results.append(is_safe(tmp_report))

        if not any(results):
            continue

        total += 1

    return total


if __name__ == '__main__':
    reports = []
    with open(INPUT_ROOT / 'day02.txt') as f:
        for line in f:
            report = [int(lvl) for lvl in line.split()]

            reports.append(report)

    print(f"{part1(reports)=}")
    print(f"{part2(reports)=}")

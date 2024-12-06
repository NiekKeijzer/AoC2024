import re

from aoc.const import INPUT_ROOT

mul_pattern = re.compile(r'mul\(\d+,\d+\)')
mul_args_pattern = re.compile(r'\d+')

def parse_arguments(match: str) -> tuple[int, int]:
    args = re.findall(mul_args_pattern, match)
    return int(args[0]), int(args[1])

def part1(lines: list[str]) -> int :
    total = 0
    for line in lines:
        matches = re.findall(mul_pattern, line)
        if not matches:
            continue

        for match in matches:
            args = parse_arguments(match)
            total += args[0] * args[1]

    return total


def part2(lines: list[str]) -> int :
    op_pattern = re.compile(r'(?:mul\(\d+,\d+\)|don\'t\(\)|do\(\))')
    total = 0
    skipping = False
    for line in lines:
        matches = re.findall(op_pattern, line)

        for match in matches:
            if match == 'don\'t()':
                skipping = True
                continue

            if match == 'do()':
                skipping = False
                continue

            if skipping:
                continue

            args = parse_arguments(match)
            total += args[0] * args[1]

    return total

if __name__ == '__main__':
    with open(INPUT_ROOT / 'day03.txt') as f :
        lines = f.readlines()

    print(f"{part1(lines)}")
    print(f"{part2(lines)}")
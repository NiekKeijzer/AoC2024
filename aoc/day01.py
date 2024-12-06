from aoc.const import INPUT_ROOT


def part1(left: list[int], right: list[int]) -> int:
    left, right = sorted(left), sorted(right)

    total = 0
    for i in range(len(left)):
        distance = abs(left[i] - right[i])
        total += distance

    return total


def part2(left: list[int], right: list[int]) -> int:
    total = 0
    for id in left:
        sim_score = id * right.count(id)

        total += sim_score

    return total


if __name__ == '__main__':
    left = []
    right = []
    with open(INPUT_ROOT / 'day01.txt') as f:
        for line in f:
            a, b = line.split('   ')
            left.append(int(a))
            right.append(int(b))

    print(f"{part1(left, right)=}")
    print(f"{part2(left, right)=}")

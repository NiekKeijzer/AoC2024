from aoc.const import INPUT_ROOT


def value_at_pos(grid, x, y):
    if x < 0 or y < 0:
        return None

    try:
        return grid[y][x]
    except IndexError:
        return None


def part1(grid) -> int:
    total = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != 'X':
                continue

            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue

                    if 'M' != value_at_pos(grid, x + dx * 1, y + dy * 1):
                        continue

                    if 'A' != value_at_pos(grid, x + dx * 2, y + dy * 2):
                        continue

                    if 'S' != value_at_pos(grid, x + dx * 3, y + dy * 3):
                        continue

                    total += 1
    return total


def part2(grid) -> int:
    total = 0
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char != 'A':
                continue

            pair_a = [value_at_pos(grid, x - 1, y - 1), value_at_pos(grid, x + 1, y + 1)]
            pair_b = [value_at_pos(grid, x + 1, y - 1), value_at_pos(grid, x - 1, y + 1)]
            if 'M' in pair_a and 'S' in pair_a and 'M' in pair_b and 'S' in pair_b:

                total += 1
    return total

if __name__ == '__main__':
    grid = []
    with open(INPUT_ROOT / 'day04.txt') as f:
        for line in f:
            grid.append(line.strip())

    print(f"{part1(grid)=}")
    print(f"{part2(grid)=}")
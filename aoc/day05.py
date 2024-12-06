from aoc.const import INPUT_ROOT

def is_valid_update(update, rules):
    for before, after in rules:
        try:
            before_idx, after_idx = update.index(before), update.index(after)
        except ValueError:
            continue

        if before_idx > after_idx:
            return False

    return True

def part1(rules, updates) -> int:
    total = 0
    for update in updates:
        if not is_valid_update(update, rules):
            continue

        middle_idx = len(update) // 2
        total += int(update[middle_idx])

    return total

def part2(rules, updates):
    total = 0

    return total

if __name__ == '__main__':
    rules = []
    updates = []

    with open(INPUT_ROOT / 'day05.txt') as f:
        rules_done = False
        for line in f:
            if line.strip() == '':
                rules_done = True
                continue

            if not rules_done:
                rules.append(line.strip().split('|'))
                continue

            if rules_done:
                updates.append(line.strip().split(','))

    print(part1(rules, updates))
    print(part2(rules, updates))
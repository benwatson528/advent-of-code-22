def solve_priority(rucksacks) -> int:
    total = 0
    for rucksack in rucksacks:
        divider = len(rucksack) // 2
        compartments = rucksack[:divider], rucksack[divider:]
        priorities = transform_priorities(compartments[0]), transform_priorities(compartments[1])
        total += sum(set(priorities[0]).intersection(set(priorities[1])))
    return total


def solve_badges(rucksacks) -> int:
    total = 0
    for group in chunks(rucksacks, 3):
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total += transform_priorities(common.pop())[0]
    return total


def transform_priorities(compartment):
    return [ord(item) - 96 if item.lower() == item else ord(item) - 38 for item in compartment]


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

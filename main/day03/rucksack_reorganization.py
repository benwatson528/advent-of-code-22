def solve(rucksacks) -> int:
    total = 0
    for rucksack in rucksacks:
        priorities = transform_priorities(rucksack[0]), transform_priorities(rucksack[1])
        total += sum(set(priorities[0]).intersection(set(priorities[1])))
    return total


def transform_priorities(compartment):
    return [ord(item) - 96 if item.lower() == item else ord(item) - 38 for item in compartment]

from collections import Counter

DIRECTIONS = [("N", "NE", "NW", "N"), ("S", "SE", "SW", "S"), ("W", "NW", "SW", "W"), ("E", "NE", "SE", "E")]
MOVEMENTS = {"N": (-1, 0), "NE": (-1, 1), "E": (0, 1), "SE": (1, 1), "S": (1, 0), "SW": (1, -1), "W": (0, -1),
             "NW": (-1, -1)}


def solve(elves, num_turns, stop_on_same=False) -> int:
    print()
    first_direction_idx = 0
    prev_elves = elves.copy()
    for i in range(num_turns):
        new_elves = take_turn(prev_elves, first_direction_idx)
        if stop_on_same and new_elves == prev_elves:
            return i + 1
        prev_elves = new_elves
        first_direction_idx = (first_direction_idx + 1) % len(DIRECTIONS)
    return score(new_elves)


def take_turn(elves, first_direction_idx):
    proposals = {}
    new_elves = elves.copy()
    for elf in elves:
        elves_nearby = find_elves_nearby(elf, elves)
        if not elves_nearby:
            continue
        else:
            if proposed_moved := propose_move(elves_nearby, elf, first_direction_idx):
                proposals[elf] = proposed_moved
    valid_proposals = remove_clashes(proposals)
    for elf, new_position in valid_proposals.items():
        new_elves.remove(elf)
        new_elves.add(new_position)
    return new_elves


def remove_clashes(proposals):
    valid_proposals = {}
    elves_to_remove = set()
    counter = Counter(proposals.values())
    for clash in [p for p, c in counter.items() if c > 1]:
        for elf, proposed_direction in proposals.items():
            if proposed_direction == clash:
                elves_to_remove.add(elf)
    for elf, proposed_direction in proposals.items():
        if elf not in elves_to_remove:
            valid_proposals[elf] = proposed_direction
    return valid_proposals


def propose_move(elves_nearby, current_position, start_direction_idx):
    if current_position == (2, 2):
        print()
    for dirs_to_check in DIRECTIONS[start_direction_idx:] + DIRECTIONS[:start_direction_idx]:
        if valid_move(dirs_to_check, elves_nearby):
            movement_r, movement_c = MOVEMENTS[dirs_to_check[3]]
            return current_position[0] + movement_r, current_position[1] + movement_c
    return None


def valid_move(dirs_to_check, elves_nearby):
    for dir_to_check in dirs_to_check[:3]:
        if dir_to_check in elves_nearby:
            return False
    return True


def find_elves_nearby(elf, elves):
    nearby = []
    if (elf[0] - 1, elf[1]) in elves:
        nearby.append('N')
    if (elf[0] - 1, elf[1] + 1) in elves:
        nearby.append('NE')
    if (elf[0], elf[1] + 1) in elves:
        nearby.append('E')
    if (elf[0] + 1, elf[1] + 1) in elves:
        nearby.append('SE')
    if (elf[0] + 1, elf[1]) in elves:
        nearby.append('S')
    if (elf[0] + 1, elf[1] - 1) in elves:
        nearby.append('SW')
    if (elf[0], elf[1] - 1) in elves:
        nearby.append('W')
    if (elf[0] - 1, elf[1] - 1) in elves:
        nearby.append('NW')
    return nearby


def score(elves):
    min_coord = min(r for r, c in elves), min(c for r, c in elves)
    max_coord = max(r for r, c in elves), max(c for r, c in elves)
    num_empty = 0
    for r in range(min_coord[0], max_coord[0] + 1):
        for c in range(min_coord[1], max_coord[1] + 1):
            if (r, c) not in elves:
                num_empty += 1
    return num_empty

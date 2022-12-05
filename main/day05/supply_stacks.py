def solve(stacks, instructions, move_separately) -> str:
    for instruction in instructions:
        if move_separately:
            move_crates_separately(instruction, stacks)
        else:
            move_crates_together(instruction, stacks)
    return ''.join(stacks[s].pop() for s in stacks)


def move_crates_separately(instruction, stacks):
    for _ in range(instruction.num_to_move):
        crate = stacks[instruction.move_from].pop()
        stacks[instruction.move_to].append(crate)


def move_crates_together(instruction, stacks):
    crates = []
    for _ in range(instruction.num_to_move):
        crates.append(stacks[instruction.move_from].pop())
    stacks[instruction.move_to].extend(reversed(crates))

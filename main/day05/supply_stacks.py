def solve(stacks, instructions, move_together) -> str:
    [move_crates(inst, stacks, move_together) for inst in instructions]
    return ''.join(stacks[s].pop() for s in stacks)


def move_crates(instruction, stacks, move_together):
    crates = []
    for _ in range(instruction.num_to_move):
        crates.append(stacks[instruction.move_from].pop())
    if move_together:
        crates.reverse()
    stacks[instruction.move_to].extend(crates)

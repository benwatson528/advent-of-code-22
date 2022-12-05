def solve(stacks, instructions) -> str:
    for instruction in instructions:
        for _ in range(instruction.num_to_move):
            crate = stacks[instruction.move_from].pop()
            stacks[instruction.move_to].append(crate)
    return ''.join(stacks[s].pop() for s in stacks)

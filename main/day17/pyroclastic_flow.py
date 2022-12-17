def solve(jet_pattern, shapes, num_turns) -> int:
    occupied = set()
    jet_idx = 0
    for i in range(num_turns):
        jet_idx = drop_block(occupied, shapes[i % len(shapes)], jet_pattern, jet_idx)
    return max(y for (x, y) in occupied) + 1


def drop_block(occupied, shape, jet_pattern, jet_idx):
    block_bottom = max(y for (x, y) in occupied) + 4 if occupied else 3
    block = update_block_position(shape, (2, block_bottom))
    can_move = True
    while can_move:
        block = move_sideways(occupied, block, jet_pattern[jet_idx % len(jet_pattern)])
        jet_idx += 1
        downwards_block = move_down(occupied, block)
        if not downwards_block:
            can_move = False
        else:
            block = downwards_block
    occupied.update(block)
    return jet_idx


def move_sideways(occupied, block, direction):
    movement = 1 if direction == ">" else -1
    updated_block = update_block_position(block, (movement, 0))
    for block_position in updated_block:
        if block_position in occupied or block_position[0] < 0 or block_position[0] > 6:
            return block
    return updated_block


def move_down(occupied, block):
    updated_block = update_block_position(block, (0, -1))
    for block_position in updated_block:
        if block_position in occupied or block_position[1] < 0:
            return None
    return updated_block


def update_block_position(block, modifier):
    block_position = set()
    for cell in block:
        block_position.add((cell[0] + modifier[0], cell[1] + modifier[1]))
    return block_position


def print_grid(occupied, block):
    print()
    min_cell, max_cell = min(0, min(y for (x, y) in occupied.union(block))), max(
        y for (x, y) in occupied.union(block)) + 1
    for j in reversed(range(min_cell, max_cell + 1)):
        print("|", end="")
        for i in range(7):
            if (i, j) in occupied:
                print("#", end="")
            elif (i, j) in block:
                print("@", end="")
            else:
                print(".", end="")
        print("|")
    print("+-------+")

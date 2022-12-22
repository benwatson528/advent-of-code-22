RIGHT_TURN = {"^": ">", ">": "v", "v": "<", "<": "^"}
LEFT_TURN = {y: x for x, y in RIGHT_TURN.items()}
DIRECTION_MOVEMENTS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
DIRECTION_SCORES = {">": 0, "v": 1, "<": 2, "^": 3}


def solve(grid, instructions, wrap_edges=False) -> int:
    if wrap_edges:
        portals = calculate_wrapping_warps(grid)
    min_r = min(r for r, c in grid.keys() if grid[(r, c)] == ".")
    min_c = min(c for r, c in grid.keys() if (min_r, c) in grid.keys() and grid[(min_r, c)] == ".")
    position = min_r, min_c
    facing = ">"
    for instruction in instructions:
        if isinstance(instruction, int):
            position = walk(grid, position, facing, int(instruction))
        else:
            facing = LEFT_TURN[facing] if instruction == "L" else RIGHT_TURN[facing]
    return ((position[0] + 1) * 1000) + ((position[1] + 1) * 4) + DIRECTION_SCORES[facing]


def walk(grid, position, facing, num_steps):
    for _ in range(num_steps):
        potential_new_position = (
            position[0] + DIRECTION_MOVEMENTS[facing][0], position[1] + DIRECTION_MOVEMENTS[facing][1])
        new_cell = grid.get(potential_new_position, None)
        # we can move
        if new_cell == "." or new_cell in DIRECTION_MOVEMENTS.keys():
            position = potential_new_position
            grid[position] = facing
        # it's a wall, stop
        elif new_cell == "#":
            return position
        # we've gone off the map
        else:
            if facing == "^":
                potential_new_position = max(r for r, c in grid if c == potential_new_position[1]), \
                    potential_new_position[1]
                if grid[potential_new_position] == '#':
                    return position
                else:
                    position = potential_new_position
                    grid[position] = facing
            elif facing == "v":
                potential_new_position = min(r for r, c in grid if c == potential_new_position[1]), \
                    potential_new_position[1]
                if grid[potential_new_position] == '#':
                    return position
                else:
                    position = potential_new_position
                    grid[position] = facing
            elif facing == "<":
                potential_new_position = potential_new_position[0], max(
                    c for r, c in grid if r == potential_new_position[0])
                if grid[potential_new_position] == '#':
                    return position
                else:
                    position = potential_new_position
                    grid[position] = facing
            elif facing == ">":
                potential_new_position = potential_new_position[0], min(
                    c for r, c in grid if r == potential_new_position[0])
                if grid[potential_new_position] == '#':
                    return position
                else:
                    position = potential_new_position
                    grid[position] = facing
    return position


def calculate_wrapping_warps(grid):
    wrappings = {}
    grid_size = max(r for (r, c) in grid) / 3
    # top 1 joins to top 2
    # top 1
    top_1_min_r = min(r for r, c in grid)
    top_1_min_c = min(c for r, c in grid if (top_1_min_r, c) in grid)
    
    # top 2
    top_2_min_c = min(c for r, c in grid)
    top_2_min_r = min(r for r, c in grid if (r, top_2_min_c) in grid)
    
    for i in top_2_min_r
        
    return wrappings | {v: k for k, v in wrappings}

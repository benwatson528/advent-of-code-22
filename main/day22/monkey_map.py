RIGHT_TURN = {"^": ">", ">": "v", "v": "<", "<": "^"}
LEFT_TURN = {y: x for x, y in RIGHT_TURN.items()}
DIRECTION_MOVEMENTS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
DIRECTION_SCORES = {">": 0, "v": 1, "<": 2, "^": 3}


def solve(grid, instructions, wrap_edges, ) -> int:
    portals = calculate_wrapping_warps(grid) if wrap_edges else {}
    min_r = min(r for r, c in grid.keys() if grid[(r, c)] == ".")
    min_c = min(c for r, c in grid.keys() if (min_r, c) in grid.keys() and grid[(min_r, c)] == ".")
    position = min_r, min_c
    facing = ">"
    grid[(min_r, min_c)] = facing
    for instruction in instructions:
        if isinstance(instruction, int):
            position, new_facing = walk(grid, position, facing, int(instruction), portals)
            if new_facing is not None:
                facing = new_facing  # if we've been turned around by hitting a portal
        else:
            facing = LEFT_TURN[facing] if instruction == "L" else RIGHT_TURN[facing]
    return ((position[0] + 1) * 1000) + ((position[1] + 1) * 4) + DIRECTION_SCORES[facing]


def walk(grid, position, facing, num_steps, portals):
    new_facing = facing
    for _ in range(num_steps):
        potential_new_position = (
            position[0] + DIRECTION_MOVEMENTS[new_facing][0], position[1] + DIRECTION_MOVEMENTS[new_facing][1])
        new_cell = grid.get(potential_new_position, None)
        temp_facing = None
        if (position, new_facing) in portals and not new_cell:
            temp_facing = new_facing
            potential_new_position, new_facing = portals[(position, new_facing)]
            new_cell = grid[potential_new_position]

        # we can move
        if new_cell == "." or new_cell in DIRECTION_MOVEMENTS.keys():
            position = potential_new_position
            grid[position] = new_facing
        # it's a wall, stop
        elif new_cell == "#":
            if temp_facing is not None:
                return position, temp_facing  # we've hit a wall on the other side so we don't want to turn
            else:
                return position, new_facing
        # we've gone off the map
        else:
            if new_facing == "^":
                potential_new_position = max(r for r, c in grid if c == potential_new_position[1]), \
                    potential_new_position[1]
                if grid[potential_new_position] == '#':
                    return position, new_facing
                else:
                    position = potential_new_position
                    grid[position] = new_facing
            elif new_facing == "v":
                potential_new_position = min(r for r, c in grid if c == potential_new_position[1]), \
                    potential_new_position[1]
                if grid[potential_new_position] == '#':
                    return position, new_facing
                else:
                    position = potential_new_position
                    grid[position] = new_facing
            elif new_facing == "<":
                potential_new_position = potential_new_position[0], max(
                    c for r, c in grid if r == potential_new_position[0])
                if grid[potential_new_position] == '#':
                    return position, new_facing
                else:
                    position = potential_new_position
                    grid[position] = new_facing
            elif new_facing == ">":
                potential_new_position = potential_new_position[0], min(
                    c for r, c in grid if r == potential_new_position[0])
                if grid[potential_new_position] == '#':
                    return position, new_facing
                else:
                    position = potential_new_position
                    grid[position] = new_facing
    return position, new_facing


# for the real input shape
def calculate_wrapping_warps(grid):
    wrappings = {}
    face_size = (max(r for (r, c) in grid) + 1) // 4
    top_5_to_left_1(face_size, wrappings)
    left_5_to_left_2(face_size, wrappings)
    top_2_to_left_4(face_size, wrappings)
    right_1_to_bottom_3(face_size, wrappings)
    right_3_to_right_6(face_size, wrappings)
    right_4_to_bottom_6(face_size, wrappings)
    bottom_1_to_top_6(face_size, wrappings)
    return wrappings


def top_5_to_left_1(face_size, wrappings):
    for i in range(face_size):
        wrappings[((0, face_size + i), "^")] = (((face_size * 3) + i, 0), ">")
        wrappings[(((face_size * 3) + i, 0), "<")] = ((0, face_size + i), "v")


def left_5_to_left_2(face_size, wrappings):
    for i in range(face_size):
        wrappings[((i, face_size), "<")] = (((face_size * 3) - i - 1, 0), ">")
        wrappings[(((face_size * 2) + i, 0), "<")] = ((face_size - i - 1, face_size), ">")


def top_2_to_left_4(face_size, wrappings):
    for i in range(face_size):
        wrappings[((face_size * 2, i), "^")] = ((face_size + i, face_size), ">")
        wrappings[((face_size + i, face_size), "<")] = ((face_size * 2, i), "v")


def right_1_to_bottom_3(face_size, wrappings):
    for i in range(face_size):
        wrappings[(((face_size * 3) + i, face_size - 1), ">")] = (((face_size * 3) - 1, face_size + i), "^")
        wrappings[(((face_size * 3) - 1, face_size + i), "v")] = (((face_size * 3) + i, face_size - 1), "<")


def right_3_to_right_6(face_size, wrappings):
    for i in range(face_size):
        wrappings[(((face_size * 2) + i, (face_size * 2) - 1), ">")] = ((face_size - i - 1, (face_size * 3) - 1), "<")
        wrappings[((face_size - i - 1, (face_size * 3) - 1), ">")] = (((face_size * 2) + i, (face_size * 2) - 1), "<")


def right_4_to_bottom_6(face_size, wrappings):
    for i in range(face_size):
        wrappings[((face_size + i, (face_size * 2) - 1), ">")] = ((face_size - 1, (face_size * 2) + i), "^")
        wrappings[((face_size - 1, (face_size * 2) + i), "v")] = ((face_size + i, (face_size * 2) - 1), "<")


def bottom_1_to_top_6(face_size, wrappings):
    for i in range(face_size):
        wrappings[(((face_size * 4) - 1, i), "v")] = ((0, (face_size * 2) + i), "v")
        wrappings[((0, (face_size * 2) + i), "^")] = (((face_size * 4) - 1, i), "^")

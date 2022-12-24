from collections import deque


def solve(start, end, blizzards, forgot_snacks) -> int:
    if forgot_snacks:
        journey_1 = dfs(start, end, blizzards, 0)
        journey_2 = dfs(end, start, blizzards, journey_1)
        return dfs(start, end, blizzards, journey_2)
    else:
        return dfs(start, end, blizzards, 0)


def dfs(start, end, blizzards, start_minute):
    grid_height, grid_width = max(start[0], end[0]), max(start[1], end[1]) + 2
    to_visit = deque()
    to_visit.append((start, start_minute))
    fastest_exit = 9999
    dead_ends = set()
    i = 0
    while to_visit:
        i += 1
        current_position, current_minute = to_visit.popleft()
        if current_position == end:
            fastest_exit = min(fastest_exit, current_minute)
            continue
        if (current_position, current_minute) in dead_ends:
            continue
        if current_minute > fastest_exit:
            continue
        if is_in_blizzard(current_position, current_minute, blizzards, (grid_height, grid_width)):
            dead_ends.add((current_position, current_minute))
            continue
        next_moves = get_next_moves(current_position, start, end, grid_height, grid_width)
        for next_position in next_moves:
            to_visit.append((next_position, current_minute + 1))
        if i % 100 == 0:
            to_visit = deque(dict.fromkeys(to_visit))
    return fastest_exit


def is_in_blizzard(current_position, minute, blizzards, grid_size):
    if minute not in blizzards["^"]:
        evolve_blizzards(blizzards, minute - 1, grid_size)
    for direction, times in blizzards.items():
        if current_position in times[minute]:
            return True
    return False


def evolve_blizzards(blizzards, previous_minute, grid_size):
    for direction, times in blizzards.items():
        for coord in times[previous_minute]:
            blizzards[direction][previous_minute + 1].add(move_coord(coord, direction, grid_size))


def move_coord(coord, direction, grid_size):
    match direction:
        case "^":
            return (grid_size[0] - 1, coord[1]) if coord[0] - 1 == 0 else (coord[0] - 1, coord[1])
        case "v":
            return (1, coord[1]) if coord[0] + 1 == grid_size[0] else (coord[0] + 1, coord[1])
        case "<":
            return (coord[0], grid_size[1] - 2) if coord[1] - 1 == 0 else (coord[0], coord[1] - 1)
        case ">":
            return (coord[0], 1) if coord[1] + 1 == grid_size[1] - 1 else (coord[0], coord[1] + 1)


def get_next_moves(current_position, start, end, grid_height, grid_width):
    return [position for position in [(current_position[0] + 1, current_position[1]),
                                      (current_position[0], current_position[1] + 1),
                                      current_position,
                                      (current_position[0] - 1, current_position[1]),
                                      (current_position[0], current_position[1] - 1)
                                      ]
            if is_valid_move(position, start, end, grid_height, grid_width)]


def is_valid_move(position, start, end, grid_height, grid_width):
    if position == end or position == start:
        return True
    if 0 < position[0] < grid_height and 0 < position[1] < grid_width - 1:
        return True
    return False

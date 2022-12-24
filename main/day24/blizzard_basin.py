from collections import deque
from functools import cmp_to_key


def solve(start, end, blizzards) -> int:
    return dfs(start, end, blizzards)


def dfs(start, end, blizzards):
    grid_height, grid_width = end[0], end[1] + 2
    to_visit = deque()
    to_visit.append((start, 0))
    fastest_exit = 861
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
        for next_position in get_next_moves(current_position, start, end, grid_height, grid_width):
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
            czord = (grid_size[0] - 1, coord[1]) if coord[0] - 1 == 0 else (coord[0] - 1, coord[1])
            return czord
        case "v":
            czord = (1, coord[1]) if coord[0] + 1 == grid_size[0] else (coord[0] + 1, coord[1])
            return czord
        case "<":
            czord = (coord[0], grid_size[1] - 2) if coord[1] - 1 == 0 else (coord[0], coord[1] - 1)
            return czord
        case ">":
            czord = (coord[0], 1) if coord[1] + 1 == grid_size[1] - 1 else (coord[0], coord[1] + 1)
            return czord


def get_next_moves(current_position, start, end, grid_height, grid_width):
    return [position for position in [(current_position[0] + 1, current_position[1]),
                                      (current_position[0], current_position[1] + 1),
                                      current_position,
                                      (current_position[0] - 1, current_position[1]),
                                      (current_position[0], current_position[1] - 1)
                                      ]
            if is_valid_move(position, start, end, grid_height, grid_width)]


def is_valid_move(position, start, end, grid_height, grid_width):
    if position == end:
        return True
    if position == start:
        return True
    if 0 < position[0] < grid_height and 0 < position[1] < grid_width - 1:
        return True
    return False

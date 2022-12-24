def solve(start, end, blizzards) -> int:
    return dfs(start, end, blizzards)


def dfs(start, end, blizzards):
    # height and width include the outer walls
    grid_height, grid_width = end[0], end[1] + 2
    to_visit = [(start, 0)]
    fastest_exit = 9999
    while to_visit:
        current_position, current_minute = to_visit.pop()
        if current_position == (1, 1):
            print()
        if current_minute > fastest_exit:
            continue
        if current_position == end:
            fastest_exit = min(fastest_exit, current_minute)
            continue
        if is_in_blizzard(current_position, current_minute, blizzards, (grid_height, grid_width)):
            continue
        for next_position in get_next_moves(current_position, end, grid_height, grid_width):
            to_visit.append((next_position, current_minute + 1))
    return fastest_exit


# still need to move the left and up in negative directions...
def is_in_blizzard(current_position, current_minute, blizzards, grid_size):
    for up_blizzard in blizzards["^"][current_position[1]]:
        if (up_blizzard - current_minute - 1) % (grid_size[0] - 1) + 1 == current_position[0]:
            return True
    for down_blizzard in blizzards["v"][current_position[1]]:
        if (down_blizzard + current_minute - 1) % (grid_size[0] - 1) + 1 == current_position[0]:
            return True
    for left_blizzard in blizzards["<"][current_position[0]]:
        if (left_blizzard - current_minute - 1) % (grid_size[1] - 2) + 1 == current_position[1]:
            return True
    for right_blizzard in blizzards[">"][current_position[0]]:
        if (right_blizzard + current_minute - 1) % (grid_size[1] - 2) + 1 == current_position[1]:
            return True
    return False


def get_next_moves(current_position, end, grid_height, grid_width):
    return [position for position in [(current_position[0] - 1, current_position[1]),
                                      (current_position[0], current_position[1] - 1),
                                      current_position,
                                      (current_position[0] + 1, current_position[1]),
                                      (current_position[0], current_position[1] + 1)]
            if is_valid_move(position, end, grid_height, grid_width)]


def is_valid_move(position, end, grid_height, grid_width):
    if position == end:
        return True
    if 0 < position[0] < grid_height and 0 < position[1] < grid_width - 1:
        return True
    return False

def solve(raw_lines, spout=(500, 0), floor_depth=None) -> int:
    clay = place_clay(raw_lines)
    lowest_clay = max(y for (x, y) in clay)
    if floor_depth:
        lowest_clay += floor_depth
        clay.update(add_floor(lowest_clay))
    sand = drop_sand(clay, set(), spout, lowest_clay)
    # print_grid(clay, sand, spout)
    return len(sand)


def add_floor(floor_depth):
    floor = set()
    for i in range(500 - floor_depth - 1, 500 + floor_depth + 1):
        floor.add((i, floor_depth))
    return floor


def drop_sand(clay, sand, spout, lowest_clay):
    resting_spot = move_grain(spout, clay, sand, lowest_clay)
    while resting_spot:
        sand.add(resting_spot)
        if resting_spot == spout:
            return sand
        resting_spot = move_grain(spout, clay, sand, lowest_clay)
    return sand


def move_grain(current_grain, clay, sand, lowest_clay):
    def update(grain, x_update, y_update):
        return grain[0] + x_update, grain[1] + y_update

    def is_empty_cell(grain):
        return grain not in clay and grain not in sand

    while True:
        if current_grain[1] + 1 > lowest_clay:
            return None  # fallen off bottom
        elif is_empty_cell(update(current_grain, 0, 1)):
            current_grain = update(current_grain, 0, 1)
        elif is_empty_cell(update(current_grain, -1, 1)):
            current_grain = update(current_grain, -1, 1)
        elif is_empty_cell(update(current_grain, 1, 1)):
            current_grain = update(current_grain, 1, 1)
        else:
            return current_grain  # resting


def place_clay(raw_lines):
    clay = set()
    for points in raw_lines:
        for segment in zip(points, points[1:]):
            x1, y1 = [int(n) for n in segment[0].split(",")]
            x2, y2 = [int(n) for n in segment[1].split(",")]
            clay.update([(i, y1) for i in range(min(x1, x2), max(x1, x2) + 1)])
            clay.update([(x1, j) for j in range(min(y1, y2), max(y1, y2) + 1)])
    return clay


def print_grid(clay, sand, spout):
    print()
    min_grid = (min(x for (x, y) in clay), 0)
    max_grid = (max(x for (x, y) in clay), max(y for (x, y) in clay))
    for j in range(min_grid[1], max_grid[1] + 2):
        print()
        for i in range(min_grid[0] - 1, max_grid[0] + 2):
            if (i, j) in clay:
                print('#', end='')
            elif (i, j) == spout:
                print('+', end='')
            elif (i, j) in sand:
                print('o', end='')
            else:
                print('.', end='')

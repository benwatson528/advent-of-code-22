def solve_visible(trees) -> int:
    num_visible = 0
    for y, _ in enumerate(trees):
        for x, t in enumerate(trees[y]):
            if is_outer(x, y, trees) or look_around_visible(x, y, t, trees):
                num_visible += 1
            else:
                num_visible += look_around_visible(x, y, t, trees)
    return num_visible


def solve_scenic(trees) -> int:
    most_scenic = 0
    for y, _ in enumerate(trees):
        for x, t in enumerate(trees[y]):
            most_scenic = max(look_around_scenic(x, y, t, trees), most_scenic)
    return most_scenic


def look_around_visible(x, y, current_tree, trees):
    taller_seen_left = False
    for i in range(x-1, -1, -1):
        if current_tree <= trees[y][i]:
            taller_seen_left = True
    if not taller_seen_left:
        return True

    taller_seen_right = False
    for i in range(x + 1, len(trees[y])):
        if current_tree <= trees[y][i]:
            taller_seen_right = True
    if not taller_seen_right:
        return True

    taller_seen_up = False
    for j in range(y-1, -1, -1):
        if current_tree <= trees[j][x]:
            taller_seen_up = True
    if not taller_seen_up:
        return True

    taller_seen_down = False
    for j in range(y + 1, len(trees)):
        if current_tree <= trees[j][x]:
            taller_seen_down = True
    if not taller_seen_down:
        return True
    return False


def look_around_scenic(x, y, current_tree, trees):
    if x == 2 and y == 3:
        print()
    num_seen_left = 0
    for i in range(x-1, -1, -1):
        if current_tree > trees[y][i]:
            num_seen_left += 1
        elif current_tree <= trees[y][i]:
            num_seen_left += 1
            break

    num_seen_right = 0
    for i in range(x+1, len(trees[y])):
        if current_tree > trees[y][i]:
            num_seen_right += 1
        elif current_tree <= trees[y][i]:
            num_seen_right += 1
            break

    num_seen_up = 0
    for j in range(y-1, -1, -1):
        if current_tree > trees[j][x]:
            num_seen_up += 1
        elif current_tree <= trees[j][x]:
            num_seen_up += 1
            break

    num_seen_down = 0
    for j in range(y+1, len(trees)):
        if current_tree > trees[j][x]:
            num_seen_down += 1
        elif current_tree <= trees[j][x]:
            num_seen_down += 1
            break
    return num_seen_left * num_seen_right * num_seen_up * num_seen_down


def is_outer(x, y, trees):
    return x == 0 or y == 0 or x == len(trees[y]) - 1 or y == len(trees) - 1

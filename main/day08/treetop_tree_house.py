def solve(trees) -> int:
    num_visible = 0
    for y, _ in enumerate(trees):
        for x, t in enumerate(trees[y]):
            if is_outer(x, y, trees):
                num_visible += 1
            else:
                around = look_around(x, y, t, trees)
                num_visible += around
    return num_visible


def look_around(x, y, current_tree, trees):
    taller_seen_left = False
    for i in range(x):
        if current_tree <= trees[y][i]:
            taller_seen_left = True
    if not taller_seen_left:
        return True

    taller_seen_right = False
    for i in range(x+1, len(trees[y])):
        if current_tree <= trees[y][i]:
            taller_seen_right = True
    if not taller_seen_right:
        return True

    taller_seen_up = False
    for j in range(y):
        if current_tree <= trees[j][x]:
            taller_seen_up = True
    if not taller_seen_up:
        return True

    taller_seen_down = False
    for j in range(y+1, len(trees)):
        if current_tree <= trees[j][x]:
            taller_seen_down = True
    if not taller_seen_down:
        return True
    return False


def is_outer(x, y, trees):
    return x == 0 or y == 0 or x == len(trees[y]) - 1 or y == len(trees) - 1

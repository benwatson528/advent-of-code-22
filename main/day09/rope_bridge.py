DIRECTIONS = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}


def solve(head_moves, num_tails=1) -> int:
    knots = ((0, 0),) * (num_tails + 1)
    tail_visited = {(0, 0)}
    for head_move in head_moves:
        direction, steps = head_move
        for _ in range(steps):
            knots = move_all(direction, knots, tail_visited)
    return len(tail_visited)


def move_all(direction, knots, tail_visited):
    modifier = DIRECTIONS[direction]
    head = knots[0][0] + modifier[0], knots[0][1] + modifier[1]
    new_knots = [head]
    for knot in knots[1:]:
        new_knots.append(move_tail(new_knots[-1], knot))
    tail_visited.add(new_knots[-1])
    return new_knots


def move_tail(head, tail):
    # x same y diff by 2
    if head[0] == tail[0] and get_abs_diff(head[1], tail[1]) >= 2:
        return tail[0], tail[1] + 1 if head[1] > tail[1] else tail[1] - 1

    # y same x diff by 2
    if head[1] == tail[1] and get_abs_diff(head[0], tail[0]) >= 2:
        return tail[0] + 1 if head[0] > tail[0] else tail[0] - 1, tail[1]

    # diagonal
    if get_abs_diff(head[0], tail[0]) > 1 or get_abs_diff(head[1], tail[1]) > 1:
        return tail[0] + 1 if head[0] > tail[0] else tail[0] - 1, \
            tail[1] + 1 if head[1] > tail[1] else tail[1] - 1

    # moving would cause us to enter the head, or we're already at the head
    return tail


def get_abs_diff(a, b):
    return max(a, b) - min(a, b)

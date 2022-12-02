def solve_move(moves) -> int:
    return sum(map(score, moves))


def solve_outcome(moves) -> int:
    updated_moves = map(find_move, moves)
    return sum(map(score, updated_moves))


def find_move(move):
    opponent, outcome = move
    if outcome == 0:
        return opponent, (opponent + 2) % 3
    elif outcome == 1:
        return opponent, opponent
    else:
        return opponent, (opponent + 1) % 3


def score(move):
    opponent, player = move
    base_score = player + 1
    if opponent == player:
        return 3 + base_score
    elif (opponent + 1) % 3 == player:
        return 6 + base_score
    else:
        return base_score

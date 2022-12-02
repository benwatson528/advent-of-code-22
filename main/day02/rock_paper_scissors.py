LOSERS = {'A': 'Z', 'B': 'X', 'C': 'Y'}
WINNERS = {'A': 'Y', 'B': 'Z', 'C': 'X'}
DRAWERS = {'A': 'X', 'B': 'Y', 'C': 'Z'}


def solve_move(moves) -> int:
    return sum(map(score, moves))


def solve_outcome(moves) -> int:
    updated_moves = map(find_move, moves)
    return sum(map(score, updated_moves))


def find_move(move):
    opponent, outcome = move
    if outcome == 'X':
        return opponent, LOSERS[opponent]
    elif outcome == 'Y':
        return opponent, DRAWERS[opponent]
    else:
        return opponent, WINNERS[opponent]


def score(move):
    opponent, player = move
    shape_score = ord(player) - 87
    if LOSERS[opponent] == player:
        return shape_score
    elif DRAWERS[opponent] == player:
        return 3 + shape_score
    else:
        return 6 + shape_score

LOSERS = {('A', 'Z'), ('B', 'X'), ('C', 'Y')}
WINNERS = {('A', 'Y'), ('B', 'Z'), ('C', 'X')}
DRAWERS = {('A', 'X'), ('B', 'Y'), ('C', 'Z')}


def solve_move(moves) -> int:
    return sum(map(score, moves))


def solve_outcome(moves) -> int:
    updated_moves = list(map(find_move, moves))
    return sum(map(score, updated_moves))


def find_move(move):
    opponent, outcome = move
    if outcome == 'X':
        return opponent, dict(LOSERS)[opponent]
    elif outcome == 'Y':
        return opponent, dict(DRAWERS)[opponent]
    else:
        return opponent, dict(WINNERS)[opponent]


def score(move):
    opponent, player = move
    shape_score = ord(player) - 87
    outcome_score = 3
    if (opponent, player) in LOSERS:
        outcome_score = 0
    elif (opponent, player) in WINNERS:
        outcome_score = 6
    return outcome_score + shape_score

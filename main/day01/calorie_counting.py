def solve(elves):
    return sorted(map(lambda l: sum(l), elves), reverse=True)

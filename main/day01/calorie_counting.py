def solve(elves, n):
    return sum(sorted(map(sum, elves), reverse=True)[:n])

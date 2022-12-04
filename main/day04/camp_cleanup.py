def solve_full_overlap(sectors) -> int:
    return sum((s[0] >= s[2] and s[1] <= s[3]) or (s[2] >= s[0] and s[3] <= s[1]) for s in sectors)


def solve_any_overlap(sectors) -> int:
    return sum(s[0] <= s[2] <= s[1] or s[2] <= s[0] <= s[3] for s in sectors)

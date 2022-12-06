def solve(s) -> int:
    windows = zip(s, s[1:], s[2:], s[3:])
    deduped = [set(list(s)) for s in windows]
    for i, e in enumerate(deduped):
        if len(e) == 4:
            return i + 4
    return -1

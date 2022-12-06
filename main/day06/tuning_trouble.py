def solve(s, num_unique) -> int:
    for i in range(len(s) - num_unique):
        deduped = set(s[i:i+num_unique])
        if len(deduped) == num_unique:
            return i + num_unique

    return -1

def solve(commands) -> int:
    signal_strength = 0
    cycle = 0
    x = 1
    for cmd in commands:
        if cmd == "noop":
            cycle += 1
            signal_strength += check_cycle(cycle, x)
        else:
            cycle += 1
            signal_strength += check_cycle(cycle, x)
            cycle += 1
            signal_strength += check_cycle(cycle, x)
            x += int(cmd.split(" ")[1])

    return signal_strength


def check_cycle(cycle, x):
    if cycle in (20, 60, 100, 140, 180, 220):
        return cycle * x

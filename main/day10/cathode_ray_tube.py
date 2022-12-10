def solve_cycle(commands) -> int:
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


def solve_draw(commands) -> list[str]:
    grid = []
    cycle = 0
    x = 1
    for cmd in commands:
        if cmd == "noop":
            grid.append(draw_pixel(cycle, x))
            cycle += 1
        else:
            grid.append(draw_pixel(cycle, x))
            cycle += 1
            grid.append(draw_pixel(cycle, x))
            cycle += 1
            x += int(cmd.split(" ")[1])
    return [''.join(grid[idx:idx + 40]) for idx in range(0, len(grid), 40)]


def draw_pixel(cycle, x):
    return '#' if cycle % 40 in range(x - 1, x + 2) else '.'


def check_cycle(cycle, x):
    return cycle * x if cycle in (20, 60, 100, 140, 180, 220) else 0

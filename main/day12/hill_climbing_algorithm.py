from collections import deque


def solve(grid, start, end) -> int:
    return bfs(grid, start, end)


def bfs(grid, start, end):
    to_visit = deque([start])
    distances = {start: 0}
    while to_visit:
        current = to_visit.popleft()
        if current == end:
            return distances[current]
        for neighbour in [(current[0] + 1, current[1]),
                          (current[0] - 1, current[1]),
                          (current[0], current[1] + 1),
                          (current[0], current[1] - 1)]:
            if not is_valid_move(grid, current, neighbour, end) \
                    or neighbour in distances:
                continue
            distances[neighbour] = distances[current] + 1
            to_visit.append(neighbour)


def is_valid_move(grid, current, neighbour, end):
    if neighbour == end and grid[current[0]][current[1]] in ('y', 'z'):
        return True
    else:
        return (0 <= neighbour[0] < len(grid) and 0 <= neighbour[1] < len(
            grid[0])) \
            and (int(ord(grid[neighbour[0]][neighbour[1]]) - int(
                ord(grid[current[0]][current[1]]))) <= 1
                 or grid[current[0]][current[1]] == 'S') \
            and neighbour != end

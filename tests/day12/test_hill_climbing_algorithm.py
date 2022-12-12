import os
from pathlib import Path

from main.day12.hill_climbing_algorithm import solve_from_start, solve_from_a


def test_from_start_simple():
    grid, start, end = read_input("data/test_input.txt")
    assert solve_from_start(grid, start, end) == 31


def test_from_start_real():
    grid, start, end = read_input("data/input.txt")
    assert solve_from_start(grid, start, end) == 497


def test_from_a_simple():
    grid, _, end = read_input("data/test_input.txt")
    assert solve_from_a(grid, end) == 29


def test_from_a_real():
    grid, _, end = read_input("data/input.txt")
    assert solve_from_a(grid, end) == 492


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        grid = f.read().splitlines()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S':
                    start = (i, j)
                elif grid[i][j] == 'E':
                    end = (i, j)
        return grid, start, end

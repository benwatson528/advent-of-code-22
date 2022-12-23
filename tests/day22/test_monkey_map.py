import os
from pathlib import Path

from main.day22.monkey_map import solve


def test_flat_simple():
    grid, instructions = read_input("data/test_input.txt")
    assert solve(grid, instructions, False) == 6032


def test_flat_real():
    grid, instructions = read_input("data/input.txt")
    assert solve(grid, instructions, False) == 76332


def test_cube_real():
    grid, instructions = read_input("data/input.txt")
    assert solve(grid, instructions, True) == 144012


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        grid = build_grid(lines[:-2])
        instructions = parse_instructions(lines[-1])
    return grid, instructions


def build_grid(lines):
    grid = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (val := lines[i][j]) != ' ':
                grid[(i, j)] = val
    return grid


def parse_instructions(raw_instructions):
    instructions = []
    number = []
    for c in raw_instructions:
        if c.isdigit():
            number.append(c)
        elif number:
            instructions.append(int(''.join(number)))
            number = []
            instructions.append(c)
    if number:
        instructions.append(int(''.join(number)))
    return instructions

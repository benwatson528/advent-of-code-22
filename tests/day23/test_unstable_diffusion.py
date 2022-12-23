import os
from pathlib import Path

from main.day23.unstable_diffusion import solve


def test_simple():
    assert solve(read_input("data/test_input.txt"), 10) == 110


def test_real():
    assert solve(read_input("data/input.txt"), 10) == 4056


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        elves = set()
        lines = f.read().splitlines()
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c] == '#':
                    elves.add((r, c))
        return elves

import os
from pathlib import Path

from main.day23.unstable_diffusion import solve


def test_ten_turns_simple():
    assert solve(read_input("data/test_input.txt"), 10, False) == 110


def test_ten_turns_real():
    assert solve(read_input("data/input.txt"), 10, False) == 4056


def test_unchanging_simple():
    assert solve(read_input("data/test_input.txt"), 100000, True) == 20


def test_unchanging_real():
    assert solve(read_input("data/input.txt"), 100000, True) == 999


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        elves = set()
        lines = f.read().splitlines()
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c] == '#':
                    elves.add((r, c))
        return elves

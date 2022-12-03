import os
from pathlib import Path

from main.day03.rucksack_reorganization import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 157


def test_real():
    assert solve(read_input("data/input.txt")) == 7990


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            stripped = line.strip('\n')
            divider = len(stripped) // 2
            lines.append((stripped[:divider], stripped[divider:]))
        return lines

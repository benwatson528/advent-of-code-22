import os
from pathlib import Path

from main.day14.regolith_reservoir import solve


def test_no_floor_simple():
    assert solve(read_input("data/test_input.txt")) == 24


def test_no_floor_real():
    assert solve(read_input("data/input.txt")) == 1072


def test_floor_simple():
    assert solve(read_input("data/test_input.txt"), floor_depth=2) == 93


def test_floor_real():
    assert solve(read_input("data/input.txt"), floor_depth=2) == 24659


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f.read().splitlines():
            lines.append(line.split(" -> "))
    return lines

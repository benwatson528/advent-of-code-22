import os
from pathlib import Path

from main.day02.rock_paper_scissors import solve_move, solve_outcome


def test_part_1_simple():
    assert solve_move(read_input("data/test_input.txt")) == 15


def test_part_1_real():
    assert solve_move(read_input("data/input.txt")) == 11767


def test_part_2_simple():
    assert solve_outcome(read_input("data/test_input.txt")) == 12


def test_part_2_real():
    assert solve_outcome(read_input("data/input.txt")) == 11767


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            stripped = line.strip('\n')
            lines.append((stripped[0], stripped[2]))
        return lines

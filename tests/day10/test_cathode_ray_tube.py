import os
from pathlib import Path

from main.day10.cathode_ray_tube import solve_cycle, solve_draw


def test_cycle_simple():
    assert solve_cycle(read_input("data/test_input.txt")) == 13140


def test_cycle_real():
    assert solve_cycle(read_input("data/input.txt")) == 11820


def test_draw_simple():
    assert solve_draw(read_input("data/test_input.txt")) == read_input("data/test_output.txt")


def test_draw_real():
    assert solve_draw(read_input("data/input.txt")) == read_input("data/real_output.txt")  # EPJBRKAH


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip("\n"))
        return lines

import os
from pathlib import Path

import pytest

from main.day18.boiling_boulders import solve_all_surface_area, solve_outer_surface_area


def test_all_simple():
    assert solve_all_surface_area(read_input("data/test_input.txt")) == 64


def test_all_real():
    assert solve_all_surface_area(read_input("data/input.txt")) == 3454


def test_inner_simple():
    assert solve_outer_surface_area(read_input("data/test_input.txt")) == 58


def test_inner_real():
    assert solve_outer_surface_area(read_input("data/input.txt")) == 2014


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = set()
        for line in f:
            lines.add(tuple((int(x) for x in line.strip('\n').split(","))))
        return lines

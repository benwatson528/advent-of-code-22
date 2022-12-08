import os
from pathlib import Path

from main.day08.treetop_tree_house import solve_visible, solve_scenic


def test_visible_simple():
    assert solve_visible(read_input("data/test_input.txt")) == 21


def test_visible_real():
    assert solve_visible(read_input("data/input.txt")) == 1825


def test_scenic_simple():
    assert solve_scenic(read_input("data/test_input.txt")) == 8


def test_scenic_real():
    assert solve_scenic(read_input("data/input.txt")) == 235200


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()

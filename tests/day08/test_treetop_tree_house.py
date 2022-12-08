import os
from pathlib import Path

from main.day08.treetop_tree_house import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 21


def test_real():
    assert solve(read_input("data/input.txt")) == 1825


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.read().splitlines()

import os
from pathlib import Path

from main.day07.no_space_left_on_device import solve_smallest, solve_biggest


def test_smallest_dirs_simple():
    assert solve_smallest(read_input("data/test_input.txt")) == 95437


def test_smallest_dirs_real():
    assert solve_smallest(read_input("data/input.txt")) == 1447046


def test_biggest_dirs_simple():
    assert solve_biggest(read_input("data/test_input.txt")) == 24933642


def test_biggest_dirs_real():
    assert solve_biggest(read_input("data/input.txt")) == 578710


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        file_content = f.read()
        return [c.lstrip().rstrip() for c in file_content.split("$")][1:]

import os
from pathlib import Path

from main.day06.tuning_trouble import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 7


def test_real():
    assert solve(read_input("data/input.txt")) == 1929


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().strip('\n')

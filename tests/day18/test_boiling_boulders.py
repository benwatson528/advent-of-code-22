import os
from pathlib import Path

from main.day18.boiling_boulders import solve


def test_small_simple():
    assert solve(read_input("data/small_test_input.txt")) == 10


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 64


def test_real():
    assert solve(read_input("data/input.txt")) == 3454


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(list(int(x) for x in line.strip('\n').split(",")))
        return lines

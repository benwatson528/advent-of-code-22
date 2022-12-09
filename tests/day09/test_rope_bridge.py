import os
from pathlib import Path

from main.day09.rope_bridge import solve


def test_one_tail_simple():
    assert solve(read_input("data/small_test_input.txt"), num_tails=1) == 13


def test_one_tail_real():
    assert solve(read_input("data/input.txt"), num_tails=1) == 5981


def test_nine_tails_simple():
    assert solve(read_input("data/large_test_input.txt"), num_tails=9) == 36


def test_nine_tails_real():
    assert solve(read_input("data/input.txt"), num_tails=9) == 2352


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            split = line.strip('\n').split(" ")
            lines.append((split[0], int(split[1])))
        return lines

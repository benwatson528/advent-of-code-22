import os
from pathlib import Path

import pytest

from main.day20.grove_positioning_system import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 3


def test_real():
    assert solve(read_input("data/input.txt")) == 4914


def test_decryption_simple():
    assert solve(read_input("data/test_input.txt"), 811589153, 10) == 1623178306


def test_decryption_small_test_input():
    assert solve(read_input("data/small_test_input.txt"), 811589153, 10) == 6492713224


@pytest.mark.skip(reason="Takes 15s to run")
def test_decryption_real():
    assert solve(read_input("data/input.txt"), 811589153, 10) == 7973051839072  # 3327515527300  # too low


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines

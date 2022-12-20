import os
from pathlib import Path

from main.day20.grove_positioning_system import solve


def test_simple():
    assert solve(read_input("data/test_input.txt")) == 3


def test_real():
    assert solve(read_input("data/input.txt")) == 4914


def test_decryption_simple():
    assert solve(read_input("data/test_input.txt"), 811589153, 10) == 1623178306


# def test_decryption_real():
#     assert solve(read_input("data/input.txt"), 811589153, 10) == 3327515527300  # 3327515527300  # too low


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(int(line.strip('\n')))
        return lines

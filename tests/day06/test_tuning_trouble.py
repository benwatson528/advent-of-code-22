import os
from pathlib import Path

from main.day06.tuning_trouble import solve


def test_packet_simple():
    assert solve(read_input("data/test_input.txt"), 4) == 7


def test_packet_real():
    assert solve(read_input("data/input.txt"), 4) == 1929


def test_message_simple():
    assert solve(read_input("data/test_input.txt"), 14) == 19


def test_message_real():
    assert solve(read_input("data/input.txt"), 14) == 3298


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().strip('\n')

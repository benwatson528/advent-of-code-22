import os
from pathlib import Path

import pytest

from main.day11.Monkey import Monkey
from main.day11.monkey_in_the_middle import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), num_rounds=20, divisor=3) == 10605


def test_p1_real():
    assert solve(read_input("data/input.txt"), num_rounds=20, divisor=3) == 55216


def test_p2_simple():
    assert solve(read_input("data/test_input.txt"), num_rounds=10000, divisor=1) == 2713310158


def test_p2_real():
    assert solve(read_input("data/input.txt"), num_rounds=10000, divisor=1) == 12848882750


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return {m.m_id: m for m in map(Monkey, f.read().split("\n\n"))}

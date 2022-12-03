import os
from pathlib import Path

from main.day03.rucksack_reorganization import solve_priority, solve_badges


def test_part_1_simple():
    assert solve_priority(read_input("data/test_input.txt")) == 157


def test_part_1_real():
    assert solve_priority(read_input("data/input.txt")) == 7990


def test_part_2_simple():
    assert solve_badges(read_input("data/test_input.txt")) == 70


def test_part_2_real():
    assert solve_badges(read_input("data/input.txt")) == 2602


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(line.strip('\n'))
        return lines

import os
import re
from pathlib import Path

from main.day04.camp_cleanup import solve_full_overlap, solve_any_overlap


def test_full_overlap_simple():
    assert solve_full_overlap(read_input("data/test_input.txt")) == 2


def test_full_overlap_real():
    assert solve_full_overlap(read_input("data/input.txt")) == 462


def test_any_overlap_simple():
    assert solve_any_overlap(read_input("data/test_input.txt")) == 4


def test_any_overlap_real():
    assert solve_any_overlap(read_input("data/input.txt")) == 835


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            lines.append(list(int(x) for x in re.findall(r'\d+', line)))
        return lines

import json
import os
from pathlib import Path

from main.day13.distress_signal import solve_pairs, solve_all

DIVIDER_PACKETS = [json.loads("[[2]]"), json.loads("[[6]]")]


def test_pairs_simple():
    assert solve_pairs(read_input("data/test_input.txt")) == 13


def test_pairs_real():
    assert solve_pairs(read_input("data/input.txt")) == 5580


def test_all_simple():
    assert solve_all(read_input("data/test_input.txt") + DIVIDER_PACKETS) == 140


def test_all_real():
    assert solve_all(read_input("data/input.txt") + DIVIDER_PACKETS) == 26200


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = []
        for line in f:
            if line != '\n':
                lines.append(json.loads(line.strip('\n')))
        return lines

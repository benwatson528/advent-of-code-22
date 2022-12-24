import os
from collections import defaultdict
from pathlib import Path

from main.day24.blizzard_basin import solve


def test_one_visit_simple():
    start, end, blizzards = read_input("data/test_input.txt")
    assert solve(start, end, blizzards, False) == 18


def test_one_visit_real():
    start, end, blizzards = read_input("data/input.txt")
    assert solve(start, end, blizzards, False) == 326


def test_return_simple():
    start, end, blizzards = read_input("data/test_input.txt")
    assert solve(start, end, blizzards, True) == 54


def test_return_real():
    start, end, blizzards = read_input("data/input.txt")
    assert solve(start, end, blizzards, True) == 976


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        blizzards = {"^": defaultdict(set), "v": defaultdict(set), "<": defaultdict(set), ">": defaultdict(set)}
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c] in ("v", "<", ">", "^"):
                    # direction -> minute -> set[coords]
                    blizzards[lines[r][c]][0].add((r, c))
                elif r == 0 and lines[r][c] == ".":
                    start = (r, c)
                elif r == len(lines) - 1 and lines[r][c] == ".":
                    end = (r, c)
        return start, end, blizzards

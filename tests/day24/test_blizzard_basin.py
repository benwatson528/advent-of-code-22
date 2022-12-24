import os
from collections import defaultdict
from pathlib import Path

from main.day24.blizzard_basin import solve


def test_simple():
    start, end, blizzards = read_input("data/test_input.txt")
    assert solve(start, end, blizzards) == 18


def test_real():
    start, end, blizzards = read_input("data/input.txt")
    assert solve(start, end, blizzards) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        blizzards = {"^": defaultdict(list), "v": defaultdict(list), "<": defaultdict(list), ">": defaultdict(list)}
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c] in ("v", "<", ">", "^"):
                    add_blizzard(blizzards, r, c, lines[r][c])
                if r == 0 and lines[r][c] == ".":
                    start = (r, c)
                elif r == len(lines) - 1 and lines[r][c] == ".":
                    end = (r, c)
        return start, end, blizzards


# blizzards_0 = up, blizzards_1 = down, blizzards_2 = left, blizzards_3 = right
def add_blizzard(blizzards, r, c, direction):
    match direction:
        case "^":
            blizzards["^"][c].append(r)
        case "v":
            blizzards["v"][c].append(r)
        case "<":
            blizzards["<"][r].append(c)
        case ">":
            blizzards[">"][r].append(c)

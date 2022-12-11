import os
import re
from pathlib import Path
from collections import defaultdict

from main.day05.Instruction import Instruction
from main.day05.supply_stacks import solve


def test_separately_simple():
    stacks, instructions = read_input("data/test_input.txt")
    assert solve(stacks, instructions, move_together=False) == "CMZ"


def test_separately_real():
    stacks, instructions = read_input("data/input.txt")
    assert solve(stacks, instructions, move_together=False) == "SHMSDGZVC"


def test_together_simple():
    stacks, instructions = read_input("data/test_input.txt")
    assert solve(stacks, instructions, move_together=True) == "MCD"


def test_together_real():
    stacks, instructions = read_input("data/input.txt")
    assert solve(stacks, instructions, move_together=True) == "VRZGHDFBQ"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw_stacks = []
        for line in f:
            if line == '\n':
                break
            raw_stacks.append(line.strip('\n'))
        stacks = process_stacks(raw_stacks)
        instructions = [
            Instruction(list(int(x) for x in re.findall(r'\d+', line)))
            for line in f]
        return stacks, instructions


def process_stacks(raw_stacks):
    stacks = defaultdict(list)
    rotated = zip(*raw_stacks[::-1])
    for row in rotated:
        if row[0].isdigit():
            stacks[int(row[0])].extend(s for s in row[1:] if s.isalpha())
    return stacks

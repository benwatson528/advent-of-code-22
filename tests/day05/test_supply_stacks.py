import os
import re
from pathlib import Path
from collections import defaultdict

from day05.Instruction import Instruction
from main.day05.supply_stacks import solve


def test_separately_simple():
    stacks, instructions = read_input("data/test_input.txt")
    assert solve(stacks, instructions, move_separately=True) == "CMZ"


def test_separately_real():
    stacks, instructions = read_input("data/input.txt")
    assert solve(stacks, instructions, move_separately=True) == "SHMSDGZVC"


def test_together_simple():
    stacks, instructions = read_input("data/test_input.txt")
    assert solve(stacks, instructions, move_separately=False) == "MCD"


def test_together_real():
    stacks, instructions = read_input("data/input.txt")
    assert solve(stacks, instructions, move_separately=False) == "SHMSDGZVC"


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw_stacks = []
        for line in f:
            if line.lstrip()[0].isdigit():
                cols = find_col_positions(line)
                break
            raw_stacks.append(line.strip('\n'))
        f.readline()
        stacks = process_stacks(reversed(raw_stacks), cols)
        instructions = [
            Instruction(list(int(x) for x in re.findall(r'\d+', line)))
            for line in f]
        return stacks, instructions


def process_stacks(raw_stacks, cols):
    stacks = defaultdict(list)
    for raw_stack in raw_stacks:
        for i in range(len(raw_stack)):
            if raw_stack[i].isalpha():
                stacks[cols[i]].append(raw_stack[i])
    return stacks


def find_col_positions(line):
    cols = {}
    for i, c in enumerate(line):
        if line[i].isdigit():
            cols[i] = int(c)
    return cols

import os
from pathlib import Path

from main.day17.pyroclastic_flow import solve


def test_p1_simple():
    assert solve(read_jet_pattern("data/test_input.txt"), read_shapes("data/blocks.txt"), 2022) == 3068


def test_p1_real():
    assert solve(read_jet_pattern("data/input.txt"), read_shapes("data/blocks.txt"), 2022) == 3219


# Part 2 solution (manual):
# Look for cycles with the same upcoming block and jet pattern index. Note that we don't care about the state of the
#  board, technically this isn't airtight but it works in this case and can be verified by seeing the cycle identifying
#  itself each turn.
# Found cycle with size = 1740 last seen 206, key = (1155, 1), current turn = 1946. Height now = 3103. Height then = 349
# 3103-349=2754 added each cycle
# 1000000000000-1946=999999998054 turns left.
# 999999998054/1740=574712642 cycles left (mod 974)
# 574712642 * 2754 = 1582758616068 height of remaining cycles + 3103 current + 1530 height from the 974 extra turns
# 206 + 974 = 1180
# height at 1180 = 1879
# 1879 - start of cycle = 1879 - 349 = 1530
# 1582758620701 right answer


def read_jet_pattern(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        return f.readline().strip("\n")[1:-1]


def read_shapes(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        shapes = []
        for raw_block in f.read().split("\n\n"):
            shape = set()
            split_raw_block = [raw for raw in raw_block.split("\n") if len(raw) != 0]
            shape_height = len(split_raw_block)
            for j in range(len(split_raw_block)):
                for i in range(len(split_raw_block[j])):
                    cell = split_raw_block[j][i]
                    if cell == '#':
                        shape.add((i, shape_height - 1 - j))
            shapes.append(shape)
    return shapes

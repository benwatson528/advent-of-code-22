import os
from pathlib import Path

from main.day17.pyroclastic_flow import solve


def test_p1_simple():
    assert solve(read_jet_pattern("data/test_input.txt"), read_shapes("data/blocks.txt"), 2022) == 3068


def test_p1_real():
    assert solve(read_jet_pattern("data/input.txt"), read_shapes("data/blocks.txt"), 2022) == 3219


def test_p2_simple():
    assert solve(read_jet_pattern("data/test_input.txt"), read_shapes("data/blocks.txt"),
                 1000000000000) == 1514285714288


def test_p2_real():
    assert solve(read_jet_pattern("data/input.txt"), read_shapes("data/blocks.txt"), 1000000000000) == -1


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

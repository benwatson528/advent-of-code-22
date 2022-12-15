import os
import re
from pathlib import Path

from main.day15.beacon_exclusion_zone import solve


def test_occupied_simple():
    assert solve(read_input("data/test_input.txt"), 10) == 26


def test_occupied_real():
    assert solve(read_input("data/input.txt"), 2000000) == 4424278


# 
# 
# def test_free_simple():
#     assert solve_p2(read_input("data/test_input.txt"), 20) == 56000011
# 
# 
# def test_free_real():
#     assert solve_p2(read_input("data/input.txt"), 4000000) == 4424278


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw = [list(int(x) for x in re.findall(r'-?\d+', line)) for line in
               f.readlines()]
        return [(x[:2], x[2:]) for x in raw]

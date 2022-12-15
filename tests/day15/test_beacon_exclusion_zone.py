import os
import re
from pathlib import Path

import pytest

from main.day15.beacon_exclusion_zone import solve, solve_p2


def test_occupied_simple():
    assert solve(read_input("data/test_input.txt"), 10) == 26


def test_occupied_real():
    assert solve(read_input("data/input.txt"), 2000000) == 4424278


@pytest.mark.skip(reason="Takes over a minute to run")
def test_free_real():
    assert solve_p2(read_input("data/input.txt"), 4000000) == 10382630753392


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        raw = [list(int(x) for x in re.findall(r'-?\d+', line)) for line in
               f.readlines()]
        return [(x[:2], x[2:]) for x in raw]

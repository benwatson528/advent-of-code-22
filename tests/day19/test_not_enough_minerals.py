import os
import re
from pathlib import Path

import pytest

from main.day19.not_enough_minerals import solve


def test_simple():
    assert solve(read_input("data/test_input.txt"), 24) == 33


@pytest.mark.skip(reason="Takes 2 minutes to run")
def test_24_turns_real():
    assert solve(read_input("data/input.txt"), 24) == 1681


@pytest.mark.skip(reason="Takes 3 minutes to run")
def test_32_turns_real():
    assert solve(read_input("data/input.txt"), 32) == 5394  # only take the first 3 Blueprints


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        costs = []
        for line in f.readlines():
            nums = [int(x) for x in re.findall(r'\d+', line)]
            costs.append({
                3: {0: nums[5], 2: nums[6]},
                2: {0: nums[3], 1: nums[4]},
                1: {0: nums[2]},
                0: {0: nums[1]}})
        return costs

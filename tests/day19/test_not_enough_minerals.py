import os
import re
from pathlib import Path

import pytest

from main.day19.not_enough_minerals import solve


@pytest.mark.skip(reason="Not working")
def test_simple():
    assert solve(read_input("data/test_input.txt"), 24) == 33


@pytest.mark.skip(reason="Not working")
def test_real():
    assert solve(read_input("data/input.txt"), 24) == 0
    # 1710 too high 1534 too low


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

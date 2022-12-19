import os
import re
from pathlib import Path

import pytest

from main.day19.not_enough_minerals import solve


@pytest.mark.skip(reason="Very slow")
def test_simple():
    assert solve(read_input("data/test_input.txt"), 24) == 33


# def test_real():
#     assert solve(read_input("data/input.txt"), 24) == 0  # 1710 too high


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        costs = []
        for line in f.readlines():
            nums = [int(x) for x in re.findall(r'\d+', line)]
            costs.append({
                "geode": {"ore": nums[5], "obsidian": nums[6]},
                "obsidian": {"clay": nums[4], "ore": nums[3]},
                "clay": {"ore": nums[2]},
                "ore": {"ore": nums[1]}})
        return costs

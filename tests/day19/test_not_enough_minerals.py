import os
import re
from pathlib import Path

from main.day19.Blueprint import Blueprint
from main.day19.not_enough_minerals import solve


def test_simple():
    assert solve(read_input("data/test_input.txt"), 15) == 33


def test_real():
    assert solve(read_input("data/input.txt"), 24) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        blueprints = []
        for line in f.readlines():
            nums = [int(x) for x in re.findall(r'\d+', line)]
            robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
            elements = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
            costs = {
                "geode": {"ore": nums[5], "obsidian": nums[6]},
                "obsidian": {"clay": nums[4], "ore": nums[3]},
                "clay": {"ore": nums[2]},
                "ore": {"ore": nums[1]}}
            blueprints.append(Blueprint(nums[0], robots, elements, costs))
        return blueprints

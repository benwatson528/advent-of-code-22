import os
import re
from pathlib import Path

from main.day16.Valve import Valve
from main.day16.proboscidea_volcanium import solve


def test_simple():
    assert solve(read_input("data/test_input.txt"), 30) == 1651


def test_real():
    assert solve(read_input("data/input.txt"), 30) == 0


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        valves = {}
        for line in f:
            matches = re.findall(r"Valve ([A-Z]+) has flow rate=(\d+); "
                                 r"tunnels? leads? to valves? (.+)", line)[0]
            valves[matches[0]] = Valve(matches[0], int(matches[1]),
                                       frozenset(matches[2].split(", ")))
        return valves

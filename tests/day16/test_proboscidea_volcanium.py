import os
import re
from pathlib import Path

import pytest

from main.day16.Valve import Valve
from main.day16.proboscidea_volcanium import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt"), 30) == 1651


@pytest.mark.skip(reason="Takes 3.5 minutes to run")
def test_p1_real():
    assert solve(read_input("data/input.txt"), 30) == 1767


# Part 2 solution:
#  1. Run part 1 over 26 turns, find the 1-person score.
#  2. Use debugger to find the open valves at the max score (1311).
#  3. Add those nodes into positive_flow_rates so they're not ignored.
#  4. Run again, adding the 1-person score to the answer.
#  Answer: 2528


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        valves = {}
        for line in f:
            matches = re.findall(r"Valve ([A-Z]+) has flow rate=(\d+); "
                                 r"tunnels? leads? to valves? (.+)", line)[0]
            valves[matches[0]] = Valve(matches[0], int(matches[1]),
                                       frozenset(matches[2].split(", ")))
        return valves

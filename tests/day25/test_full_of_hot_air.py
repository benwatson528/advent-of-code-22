import os
from pathlib import Path

from main.day25.full_of_hot_air import solve


def test_p1_simple():
    assert solve(read_input("data/test_input.txt")) == "2=-1=0"


def test_p1_real():
    assert solve(read_input("data/input.txt")) == "2=020-===0-1===2=020"


# no p2 Merry Christmas

def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        lines = f.read().splitlines()
        return lines

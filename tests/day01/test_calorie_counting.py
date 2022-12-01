import os
from pathlib import Path

from main.day01.calorie_counting import solve


def test_biggest_elf_simple():
    assert solve(read_input("data/test_input.txt"))[0] == 24000


def test_part_1_real():
    assert solve(read_input("data/input.txt"))[0] == 68787


def test_part_1_simple():
    assert sum(solve(read_input("data/test_input.txt"))[:3]) == 45000


def test_part_2_real():
    assert sum(solve(read_input("data/input.txt"))[:3]) == 198041


def read_input(file_name):
    with open(os.path.join(Path(__file__).parent.absolute(), file_name)) as f:
        elves = []
        current_elf = []
        for line in f:
            stripped = line.strip('\n')
            if len(stripped) == 0:
                elves.append(current_elf)
                current_elf = []
            else:
                current_elf.append(int(stripped))
        elves.append(current_elf)
        return elves

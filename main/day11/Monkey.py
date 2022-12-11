import re


class Monkey:
    m_id: int
    held_items: list[int]
    operation: str
    test_condition: int
    monkey_if_true: int
    monkey_if_false: int
    num_inspected: int = 0

    def __init__(self, raw):
        split_monkey = raw.split("\n")
        self.m_id = int(re.findall(r'\d+', split_monkey[0])[0])
        d = dict(x.strip().split(": ") for x in split_monkey[1:6])
        self.held_items = [int(s) for s in d["Starting items"].split(", ")]
        self.operation = d["Operation"].split(" = ")[1]
        self.test_condition = int(d["Test"].split(" by ")[1])
        self.monkey_if_true = int(d["If true"].split(" monkey ")[1])
        self.monkey_if_false = int(d["If false"].split(" monkey ")[1])

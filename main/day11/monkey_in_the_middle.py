import math


def solve(monkeys, num_rounds=20) -> int:
    for _ in range(num_rounds):
        take_turn(monkeys)
    return math.prod(sorted([m.num_inspected for m in monkeys.values()], reverse=True)[:2])


def take_turn(monkeys):
    for m_id, m in monkeys.items():
        for item in m.held_items:
            m.num_inspected += 1
            new_item, recipient = process_item(m, item)
            monkeys[recipient].held_items.append(new_item)
        m.held_items = []
    return -1


def process_item(monkey, item):
    # required for the eval
    old = item
    new = int(eval(monkey.operation))
    new = new // 3
    recipient = monkey.monkey_if_true if new % monkey.test_condition == 0 else monkey.monkey_if_false
    return new, recipient

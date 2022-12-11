import math


def solve(monkeys, num_rounds, divisor) -> int:
    lcm = math.lcm(*[m.test_condition for m in monkeys.values()])
    for _ in range(num_rounds):
        take_turn(monkeys, divisor, lcm)
    return math.prod(sorted([m.num_inspected for m in monkeys.values()], reverse=True)[:2])


def take_turn(monkeys, divisor, lcm):
    for m_id, m in monkeys.items():
        for item in m.held_items:
            m.num_inspected += 1
            new_item, recipient = process_item(m, item, divisor, lcm)
            monkeys[recipient].held_items.append(new_item)
        m.held_items = []


def process_item(monkey, old, divisor, lcm):
    new = (int(eval(monkey.operation)) // divisor) % lcm
    return (new, monkey.monkey_if_true) if new % monkey.test_condition == 0 else (new, monkey.monkey_if_false)

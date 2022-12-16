from functools import cache

valves = {}
positive_flow_rates = set()


def solve(invalves, num_turns) -> int:
    global valves
    valves = invalves
    global positive_flow_rates
    positive_flow_rates = set(valve.id for valve in valves.values() if valve.flow_rate != 0)
    return traverse(valves["AA"], num_turns, 0, frozenset(), 0)


def solve_elephant(invalves, num_turns) -> int:
    global valves
    valves = invalves
    global positive_flow_rates
    positive_flow_rates = set(valve.id for valve in valves.values() if valve.flow_rate != 0)
    return traverse_elephant(valves["AA"], valves["AA"], num_turns, 0, frozenset(), 0)


@cache
def traverse_elephant(current_elf, current_elephant, num_turns, current_turn, open_valves, flow_rate):
    if current_turn >= num_turns or (current_elf is None and current_elephant is None):
        return flow_rate
    max_flow_rate = 0
    if current_elf is not None:
        if current_elf.id in positive_flow_rates and current_elf.id not in open_valves:
            # Stay where you are and open the valve, costing one move. Don't count the new valve yet
            max_flow_rate = max(
                traverse_elephant(current_elf, current_elephant, num_turns, current_turn + 1,
                                  open_valves.union((current_elf.id,)),
                                  calc_flow_rate(open_valves, flow_rate)), max_flow_rate)
        for neighbour in current_elf.children:
            max_flow_rate = max(
                traverse_elephant(valves[neighbour], current_elephant, num_turns, current_turn + 1, open_valves,
                                  calc_flow_rate(open_valves, flow_rate)), max_flow_rate)

    if current_elephant is not None:
        if current_elephant.id in positive_flow_rates and current_elephant.id not in open_valves:
            # Stay where you are and open the valve, costing one move. Don't count the new valve yet
            max_flow_rate = max(
                traverse_elephant(current_elf, current_elephant, num_turns, current_turn + 1,
                                  open_valves.union((current_elephant.id,)),
                                  calc_flow_rate(open_valves, flow_rate)), max_flow_rate)
        for neighbour in current_elephant.children:
            max_flow_rate = max(
                traverse_elephant(current_elf, valves[neighbour], num_turns, current_turn + 1, open_valves,
                                  calc_flow_rate(open_valves, flow_rate)), max_flow_rate)
    return max_flow_rate


@cache
def traverse(current, num_turns, current_turn, open_valves, flow_rate):
    if current_turn >= num_turns or current is None:
        return flow_rate
    max_flow_rate = 0
    if current.id in positive_flow_rates and current.id not in open_valves:
        # Stay where you are and open the valve, costing one move. Don't count the new valve yet
        max_flow_rate = max(
            traverse(current, num_turns, current_turn + 1, open_valves.union((current.id,)),
                     calc_flow_rate(open_valves, flow_rate)), max_flow_rate)
    for neighbour in current.children:
        max_flow_rate = max(
            traverse(valves[neighbour], num_turns, current_turn + 1, open_valves,
                     calc_flow_rate(open_valves, flow_rate)), max_flow_rate)
    return max_flow_rate


def calc_flow_rate(open_valves, flow_rate):
    for open_valve in open_valves:
        flow_rate += valves[open_valve].flow_rate
    return flow_rate

from functools import cache

valves = {}
positive_flow_rates = set()


def solve(invalves, num_turns) -> int:
    global valves
    valves = invalves
    global positive_flow_rates
    positive_flow_rates = set(valve.id for valve in valves.values() if valve.flow_rate != 0)
    return traverse(valves["AA"], num_turns, 0, frozenset(), 0)


@cache
def traverse(current, num_turns, current_turn, open_valves, flow_rate):
    if current_turn >= 30 or current is None:
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

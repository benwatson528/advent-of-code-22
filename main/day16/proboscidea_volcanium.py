from functools import cache


def solve(valves, num_turns) -> int:
    return traverse(valves, get_valve("AA", valves), num_turns, 0, frozenset(), 0)


@cache
def traverse(valves, current, num_turns, current_turn, open_valves, flow_rate):
    # print(f"current turn = {current_turn}, open_valves = {open_valves}")
    if current_turn >= 30 or current is None:
        return flow_rate
    max_flow_rate = 0
    if current.id != "AA" and current.id not in open_valves:
        # stay where you are and open the valve, costing one move. Don't count the new valve yet
        max_flow_rate = max(
            traverse(valves, current, num_turns, current_turn + 1, open_valves.union((current.id,)),
                     calc_flow_rate(valves, open_valves, flow_rate)), max_flow_rate)
    for neighbour in current.children:
        neighbour_valve = get_valve(neighbour, valves)
        max_flow_rate = max(
            traverse(valves, neighbour_valve, num_turns, current_turn + 1, open_valves,
                     calc_flow_rate(valves, open_valves, flow_rate)), max_flow_rate)
    return max_flow_rate


def calc_flow_rate(valves, open_valves, flow_rate):
    for open_valve in open_valves:
        flow_rate += get_valve(open_valve, valves).flow_rate
    return flow_rate


def get_valve(valve_id, valves):
    for valve in valves:
        if valve_id == valve.id:
            return valve

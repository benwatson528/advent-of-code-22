from functools import cache


def solve(valves, num_turns) -> int:
    max_flow_rate = traverse(valves, get_valve("AA", valves), num_turns, 0,
                             frozenset())
    return max_flow_rate


@cache
def traverse(valves, current, num_turns, current_turn, open_valves):
    print(f"current turn = {current_turn}, open_valves = {open_valves}")
    if current_turn >= 30:
        return calculate_flow_rate(valves, open_valves, num_turns)
    max_path = 0
    for i in range(current_turn, num_turns):
        if current is None:
            return calculate_flow_rate(valves, open_valves, num_turns)
        for neighbour in current.children:
            if current.id not in [v[0] for v in open_valves]:
                union = open_valves.union(((current.id, i + 1), ))
                max_path = max(traverse(valves, get_valve(neighbour, valves),
                                        num_turns, i + 2, union), max_path)
            max_path = max(
                traverse(valves, get_valve(neighbour, valves), num_turns, i + 1,
                         open_valves), max_path)
    return calculate_flow_rate(valves, open_valves, num_turns)


def calculate_flow_rate(graph, open_valves, num_turns):
    flow_rate = 0
    for open_valve in open_valves:
        valve_id, turn_opened = open_valve[0], open_valve[1]
        valve_rate = get_valve(valve_id, graph).flow_rate
        flow_rate += valve_rate * (num_turns - turn_opened)
    return flow_rate


def get_valve(valve_id, valves):
    for valve in valves:
        if valve_id == valve.id:
            return valve

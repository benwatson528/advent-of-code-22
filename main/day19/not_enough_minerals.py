import copy
from functools import cache

COST = {}
NUM_MINUTES = 0


def solve(blueprints, num_minutes) -> int:
    print()
    robots = (1, 0, 0, 0)
    elements = (0, 0, 0, 0)
    output_geodes = []
    for i, cost in enumerate(blueprints):
        global COST
        COST = cost
        global NUM_MINUTES
        NUM_MINUTES = num_minutes
        output_geodes.append(run_blueprint(robots, elements, i, 1, frozenset()))
        print(f"Blueprint {i + 1} has {output_geodes[i]} geodes")

    return calculate_quality_level(output_geodes)


@cache
def run_blueprint(robots, elements, id, current_minute, chose_not_to_create):
    if current_minute > NUM_MINUTES:
        return elements[3]

    max_num_geodes = 0
    next_paths = []

    chose_not_to_create_now = set()
    if can_create_robot(3, elements):
        next_paths.append(create_robot(3, robots, elements))
    else:
        if can_create_robot(2, elements):
            if 2 in chose_not_to_create:
                return max_num_geodes
            next_paths.append(create_robot(2, robots, elements))
            chose_not_to_create_now.add(2)
        if can_create_robot(1, elements) and robots[1] <= 14:
            if 1 in chose_not_to_create:
                return max_num_geodes
            next_paths.append(create_robot(1, robots, elements))
            chose_not_to_create_now.add(1)
        if can_create_robot(0, elements) and robots[0] <= 4:
            if 0 in chose_not_to_create:
                return max_num_geodes
            next_paths.append(create_robot(0, robots, elements))
            chose_not_to_create_now.add(0)
        next_paths.append((robots, elements, chose_not_to_create_now))

    for next_robot, next_elements, chose_not_to_create_now2 in next_paths:
        mined_elements = mine(robots, next_elements)
        max_num_geodes = max(
            run_blueprint(next_robot, mined_elements, id, current_minute + 1, frozenset(chose_not_to_create_now2)),
            max_num_geodes)

    return max_num_geodes


def mine(robots, elements):
    new_elements = list(elements)
    for robot_type, num_of_robot in enumerate(robots):
        new_elements[robot_type] += num_of_robot
    return tuple(new_elements)


def can_create_robot(robot_type, elements):
    for element, cost in COST[robot_type].items():
        if elements[element] < cost:
            return False
    return True


def create_robot(robot_type, robots, elements):
    new_robots = list(robots)
    new_robots[robot_type] += 1
    new_elements = list(elements)
    for element_type, element_cost in COST[robot_type].items():
        new_elements[element_type] -= element_cost
    return tuple(new_robots), tuple(new_elements), frozenset()


def calculate_quality_level(geodes):
    quality_level = 0
    for i, geode in enumerate(geodes):
        quality_level += ((i + 1) * geode)
    return quality_level

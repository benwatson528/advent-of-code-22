import copy
from functools import cache

COST = {}
NUM_TURNS = 0
MAPPING = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


def solve(blueprints, num_turns) -> int:
    robots = (1, 0, 0, 0)
    elements = (0, 0, 0, 0)
    output_geodes = []
    for i, cost in enumerate(blueprints):
        global COST
        COST = cost
        global NUM_TURNS
        NUM_TURNS = num_turns
        output_geodes.append(run_blueprint(robots, elements, i + 1, 1))

    return calculate_quality_level(output_geodes)


@cache
def run_blueprint(robots, elements, id, current_turn):
    if current_turn > NUM_TURNS:
        return elements[3]
    max_num_geodes = 0
    next_paths = []
    if can_create_robot("geode", elements):
        next_paths.append(create_robot("geode", robots, elements))
    else:
        if can_create_robot("obsidian", elements) and robots[2] < 21 and elements[2] < 21:
            next_paths.append(create_robot("obsidian", robots, elements))
        if can_create_robot("clay", elements) and robots[1] < 21 and elements[1] < 21:
            next_paths.append(create_robot("clay", robots, elements))
        if can_create_robot("ore", elements) and robots[0] < 5 and elements[0] < 5:
            next_paths.append(create_robot("ore", robots, elements))
        next_paths.append((robots, elements))

    for next_robot, next_elements in next_paths:
        max_num_geodes = max(run_blueprint(next_robot, mine(robots, next_elements), id, current_turn + 1),
                             max_num_geodes)

    return max_num_geodes


def mine(robots, elements):
    new_elements = list(elements)
    for robot_type, num_of_robot in enumerate(robots):
        new_elements[robot_type] += num_of_robot
    return tuple(new_elements)


def can_create_robot(robot_type, elements):
    for element, cost in COST[robot_type].items():
        if elements[MAPPING[element]] < cost:
            return False
    return True


def create_robot(robot_type, robots, elements):
    robots_idx = MAPPING[robot_type]
    new_robots = list(robots)
    new_robots[robots_idx] = robots[robots_idx] + 1
    new_elements = list(elements)
    for element_type, element_cost in COST[robot_type].items():
        new_elements[MAPPING[element_type]] -= element_cost
    return tuple(new_robots), tuple(new_elements)


def calculate_quality_level(geodes):
    print()
    quality_level = 0
    for i, geode in enumerate(geodes):
        print(f"blueprint {i + 1} has {geode} geodes")
        quality_level += ((i + 1) * geode)
    return quality_level

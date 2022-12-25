from functools import cache

COST = {}
NUM_MINUTES = 0
MAX_NEEDED = []
MAX_GEODES = []


def solve(blueprints, num_minutes) -> int:
    robots = (1, 0, 0, 0)
    elements = (0, 0, 0, 0)
    output_geodes = []

    for i, cost in enumerate(blueprints):
        global COST
        COST = cost
        global MAX_GEODES
        max_geodes_for_blueprint = [0]
        MAX_GEODES = max_geodes_for_blueprint
        global NUM_MINUTES
        NUM_MINUTES = num_minutes
        max_needed = [0, 0, 0]
        for c in COST.values():
            for element_type, element_cost in c.items():
                if element_cost > max_needed[element_type]:
                    max_needed[element_type] = element_cost
        global MAX_NEEDED
        # don't make a robot if we already have enough of them to make enough per round to build any other robot
        MAX_NEEDED = max_needed

        output_geodes.append(run_blueprint(robots, elements, i, 1))
        print(f"Blueprint {i + 1} has {output_geodes[i]} geodes")

    return calculate_quality_level(output_geodes)


@cache
def run_blueprint(robots, elements, id, current_minute):
    if current_minute > NUM_MINUTES:
        if elements[3] > MAX_GEODES[0]:
            MAX_GEODES[0] = elements[3]
        return elements[3]
    # prune if we couldn't possibly make enough geodes even by making a new geode robot per minute
    minutes_left = NUM_MINUTES - current_minute + 1
    # how much geode we have + 1 geode per existing robot per minute + 1 + 2 + 3...
    max_possible_geodes_by_end = elements[3] + (robots[3] * minutes_left) + sum(range(minutes_left))
    if max_possible_geodes_by_end < MAX_GEODES[0]:
        return elements[3]
    max_num_geodes = 0
    next_paths = []
    # last minute - 1, only try to make geode
    if current_minute == NUM_MINUTES - 1:
        if can_create_robot(3, elements):
            next_paths.append(create_robot(3, robots, elements))
    # last minute, don't make a robot
    elif current_minute != NUM_MINUTES:
        # always make a geode robot if we can
        if can_create_robot(3, elements):
            next_paths.append(create_robot(3, robots, elements))
        else:
            if can_create_robot(2, elements) and robots[2] < MAX_NEEDED[2]:
                next_paths.append(create_robot(2, robots, elements))
            if can_create_robot(1, elements) and robots[1] < MAX_NEEDED[1]:
                next_paths.append(create_robot(1, robots, elements))
            if can_create_robot(0, elements) and current_minute != NUM_MINUTES - 2 and robots[0] < MAX_NEEDED[0]:
                next_paths.append(create_robot(0, robots, elements))

    # always do nothing
    next_paths.append((robots, elements))

    for next_robot, next_elements in next_paths:
        mined_elements = mine(robots, next_elements)
        max_num_geodes = max(run_blueprint(next_robot, mined_elements, id, current_minute + 1), max_num_geodes)

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
    return tuple(new_robots), tuple(new_elements)


def calculate_quality_level(geodes):
    quality_level = 0
    for i, geode in enumerate(geodes):
        quality_level += ((i + 1) * geode)
    return quality_level

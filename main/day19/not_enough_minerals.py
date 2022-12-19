import copy


def solve(blueprints, num_turns) -> int:
    output_blueprints = []
    for blueprint in blueprints:
        output_blueprints.append(run_blueprint(blueprint, 0, num_turns))
        print(f"Processed blueprint {blueprint}")

    return calculate_quality_level(output_blueprints)


def run_blueprint(blueprint, current_turn, num_turns):
    max_geodes_mined_blueprint = blueprint
    if current_turn < num_turns:
        blueprint.mine()
        # mine each element that we could mine
        for robot in blueprint.robots.keys():
            if blueprint.can_create_robot(robot):
                blueprint_copy = copy.deepcopy(blueprint)
                blueprint_copy.create_robot(robot)
                max_geodes_mined_blueprint = get_blueprint_with_max_geode(
                    run_blueprint(blueprint_copy, current_turn + 1, num_turns),
                    max_geodes_mined_blueprint)

        # do nothing
        blueprint_copy = copy.deepcopy(blueprint)
        max_geodes_mined_blueprint = get_blueprint_with_max_geode(
            run_blueprint(blueprint_copy, current_turn + 1, num_turns),
            max_geodes_mined_blueprint)
    return max_geodes_mined_blueprint


def get_blueprint_with_max_geode(blueprint, max_geodes_mined_blueprint):
    if blueprint.elements["geode"] > max_geodes_mined_blueprint.elements[
        "geode"]:
        return blueprint
    else:
        return max_geodes_mined_blueprint


def calculate_quality_level(blueprints):
    print()
    quality_level = 0
    for blueprint in blueprints:
        print(f"final blueprint = {blueprint}")
        quality_level += (blueprint.id * blueprint.elements["geode"])
    return quality_level

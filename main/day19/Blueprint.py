import dataclasses


@dataclasses.dataclass
class Blueprint:
    id: int
    costs = {}
    robots = {}
    elements = {}

    def __init__(self, id, robots, elements, costs):
        self.id = id
        self.robots = robots.copy()
        self.elements = elements.copy()
        self.costs = costs.copy()

    def can_create_robot(self, robot_type):
        for element, cost in self.costs[robot_type].items():
            if self.elements[element] <= cost:
                return False
        return True

    def create_robot(self, robot_type):
        self.robots[robot_type] += 1
        for element_type, element_cost in self.costs[robot_type].items():
            self.elements[element_type] -= element_cost

    def mine(self):
        for robot_type, num_of_robot in self.robots.items():
            self.elements[robot_type] += num_of_robot

    def __str__(self):
        return f"Blueprint {self.id} has robots {self.robots} and elements: {self.elements}"

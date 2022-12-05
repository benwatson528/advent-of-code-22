import dataclasses


@dataclasses.dataclass
class Instruction:
    num_to_move: int
    move_from: int
    move_to: int

    def __init__(self, raw_nums):
        self.num_to_move = raw_nums[0]
        self.move_from = raw_nums[1]
        self.move_to = raw_nums[2]

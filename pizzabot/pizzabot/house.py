from pizzabot.instruction import create_instruction

class House:
    """Class that holds house coordinates and makes small computations connected with the houses"""

    def __init__(self, X: int, Y: int):
        self.X = X
        self.Y = Y

    def distance(self, to_house: 'House') -> int:
        """Manhattan distance between this house and to_house"""
        return abs(self.X - to_house.X) + abs(self.Y - to_house.Y)

    def instructions(self, to_house: 'House') -> list['Instruction']:
        """All instructions between this house and to_house"""
        instructions = []

        horizontal_distance = to_house.X - self.X
        step = 1 if horizontal_distance > 0 else -1
        for i in range(abs(horizontal_distance)):
            instructions.append(create_instruction(step, 0))

        vertical_distance = to_house.Y - self.Y
        step = 1 if vertical_distance > 0 else -1
        for i in range(abs(vertical_distance)):
            instructions.append(create_instruction(0, step))

        instructions.append(create_instruction())
        return instructions
from pizzabot.errors import NotSupportedInstructionError

class Instruction:
    """Class used for storing the instruction's info"""

    def __init__(self, horizontal_steps, vertical_steps, full_description, short_description):
        self.horizontal_steps = horizontal_steps
        self.vertical_steps = vertical_steps
        self.full_description = full_description
        self.short_description = short_description


def create_instruction(horizontal_steps: int = 0, vertical_steps: int = 0) -> Instruction:
    """Creates an instruction using the existing types of instructions"""
    supported_instructions = {
        0: {
            0: ("Drop pizza", "D"),
            1: ("Move north", "N"),
            -1: ("Move south", "S")
        },
        1: {
            0: ("Move east", "E")
        },
        -1: {
            0: ("Move west", "W")
        }
    }

    if (horizontal_steps not in supported_instructions) or (vertical_steps not in supported_instructions[horizontal_steps]):
        raise NotSupportedInstructionError("Five instructions are supported, use one of these: (0, 0), (0, 1), (0, -1), (1, 0), and (-1, 0).")

    instruction = supported_instructions[horizontal_steps][vertical_steps]
    return Instruction(horizontal_steps, vertical_steps, instruction[0], instruction[1])
import unittest
from pizzabot.instruction import create_instruction
from pizzabot.errors import NotSupportedInstructionError

class InstructionTestSuite(unittest.TestCase):
    """Instruction test cases"""

    def test_create_instruction_1(self):
        # Arrange
        horizontal_steps = 0
        vertical_steps = 0

        # Act
        instruction = create_instruction(horizontal_steps, vertical_steps)

        # Assert
        self.assertEqual(instruction.short_description, "D")

    def test_create_instruction_2(self):
        # Arrange
        horizontal_steps = 0
        vertical_steps = 1

        # Act
        instruction = create_instruction(horizontal_steps, vertical_steps)

        # Assert
        self.assertEqual(instruction.short_description, "N")

    def test_create_instruction_3(self):
        # Arrange
        def helper():
            horizontal_steps = 0
            vertical_steps = 3
            create_instruction(horizontal_steps, vertical_steps)

        # Act & Assert
        self.assertRaises(NotSupportedInstructionError, helper)

    def test_create_instruction_4(self):
        # Arrange
        def helper():
            horizontal_steps = 2
            vertical_steps = -1
            create_instruction(horizontal_steps, vertical_steps)

        # Act & Assert
        self.assertRaises(NotSupportedInstructionError, helper)

if __name__ == '__main__':
    unittest.main()
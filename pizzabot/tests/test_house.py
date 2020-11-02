import unittest
from pizzabot.house import House

class HouseTestSuite(unittest.TestCase):
    """House test cases"""

    def test_distance_1(self):
        # Arrange
        from_house = House(0, 0)
        to_house = House(1, 3)

        # Act
        distance = from_house.distance(to_house)

        # Assert
        self.assertEqual(distance, 4)

    def test_distance_2(self):
        # Arrange
        from_house = House(3, 2)
        to_house = House(2, 4)

        # Act
        distance = from_house.distance(to_house)

        # Assert
        self.assertEqual(distance, 3)

    def test_instructions_1(self):
        # Arrange
        from_house = House(1, 0)
        to_house = House(3, 0)

        # Act
        instructions = from_house.instructions(to_house)
        text_instructions = convert_to_text_instructions(instructions)

        # Assert
        self.assertEqual(text_instructions, "EED")

    def test_instructions_2(self):
        # Arrange
        from_house = House(0, 0)
        to_house = House(0, 3)

        # Act
        instructions = from_house.instructions(to_house)
        text_instructions = convert_to_text_instructions(instructions)

        # Assert
        self.assertEqual(text_instructions, "NNND")

    def test_instructions_3(self):
        # Arrange
        from_house = House(2, 0)
        to_house = House(0, 0)

        # Act
        instructions = from_house.instructions(to_house)
        text_instructions = convert_to_text_instructions(instructions)

        # Assert
        self.assertEqual(text_instructions, "WWD")

    def test_instructions_4(self):
        # Arrange
        from_house = House(0, 4)
        to_house = House(0, 1)

        # Act
        instructions = from_house.instructions(to_house)
        text_instructions = convert_to_text_instructions(instructions)

        # Assert
        self.assertEqual(text_instructions, "SSSD")

    def test_instructions_5(self):
        # Arrange
        from_house = House(5, 5)
        to_house = House(5, 5)

        # Act
        instructions = from_house.instructions(to_house)
        text_instructions = convert_to_text_instructions(instructions)

        # Assert
        self.assertEqual(text_instructions, "D")

    def test_instructions_6(self):
        # Arrange
        from_house = House(2, 5)
        to_house = House(4, 1)

        # Act
        instructions = from_house.instructions(to_house)
        text_instructions = convert_to_text_instructions(instructions)

        # Assert
        self.assertEqual(text_instructions, "EESSSSD")

def convert_to_text_instructions(instructions):
    return "".join([instruction.short_description for instruction in instructions])

if __name__ == '__main__':
    unittest.main()
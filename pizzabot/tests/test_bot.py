import unittest
from pizzabot.bot import Bot
from pizzabot.input import InputType, create_input

class BotTestSuite(unittest.TestCase):
    """Bot test cases"""

    def test_get_text_instructions_1(self):
        # Arrange
        string = "3x3 (1, 2)"
        string_input = create_input(InputType.StringInput)
        string_input.add_string(string)
        bot = Bot(string_input)

        # Act
        text_instructions = bot.get_text_instructions()

        # Assert
        self.assertEqual(text_instructions, "ENND")

    def test_get_text_instructions_2(self):
        # Arrange
        string = "5x5 (1, 3) (4, 4)"
        string_input = create_input(InputType.StringInput)
        string_input.add_string(string)
        bot = Bot(string_input)

        # Act
        text_instructions = bot.get_text_instructions()

        # Assert
        self.assertEqual(text_instructions, "ENNNDEEEND")

    def test_get_text_instructions_3(self):
        # Arrange
        string = "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
        string_input = create_input(InputType.StringInput)
        string_input.add_string(string)
        bot = Bot(string_input)

        # Act
        text_instructions = bot.get_text_instructions()

        # Assert
        self.assertEqual(text_instructions, "DNDENNDEDESDEDDSDNNND")


    def test_get_text_instructions_4(self):
        # Arrange
        file_path ="tests//resources//test_file.txt"
        file_input = create_input(InputType.FileReadInput)
        file_input.add_file_path(file_path)
        bot = Bot(file_input)

        # Act
        text_instructions = bot.get_text_instructions()

        # Assert
        self.assertEqual(text_instructions, "ENNNDEEEND")

if __name__ == '__main__':
    unittest.main()
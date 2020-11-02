import unittest
from pizzabot.input import InputType, create_input, FileReadInput
from pizzabot.errors import NotSupportedInputTypeError, MissingPropertyError, BadInputFormatError, BadHouseCoordinatesError

class InputTestSuite(unittest.TestCase):
    """Input test cases"""

    def test_create_input_1(self):
        # Arrange
        input_type = InputType.FileReadInput

        # Act
        file_input = create_input(input_type)

        # Assert
        self.assertIsInstance(file_input, FileReadInput)

    def test_create_input_2(self):
        # Arrange
        def helper():
            input_type = "something random"
            random_input = create_input(input_type)

        # Act & Assert
        self.assertRaises(NotSupportedInputTypeError, helper)

    def test_StringInput_1(self):
        # Arrange
        input_type = InputType.StringInput
        string = "text"

        # Act
        string_input = create_input(input_type)
        string_input.add_string(string)

        # Assert
        self.assertEqual(string_input.string, string)

    def test_StringInput_2(self):
        # Arrange
        def helper():
            input_type = InputType.StringInput
            string_input = create_input(input_type)
            string_input.get_houses()

        # Act & Assert
        self.assertRaises(MissingPropertyError, helper)

    def test_FileReadInput_1(self):
        # Arrange
        input_type = InputType.FileReadInput
        file_path = "text"

        # Act
        file_input = create_input(input_type)
        file_input.add_file_path(file_path)

        # Assert
        self.assertEqual(file_input.file_path, file_path)

    def test_FileReadInput_2(self):
        # Arrange
        def helper():
            input_type = InputType.FileReadInput
            file_input = create_input(input_type)
            file_input.get_houses()

        # Act & Assert
        self.assertRaises(MissingPropertyError, helper)

    def test_FileReadInput_3(self):
        # Arrange
        def helper():
            input_type = InputType.FileReadInput
            file_path = "something random"
            file_input = create_input(input_type)
            file_input.add_file_path(file_path)
            file_input.get_houses()

        # Act & Assert
        self.assertRaises(FileNotFoundError, helper)

    def test_FileReadInput_4(self):
        # Arrange
        def helper():
            input_type = InputType.FileReadInput
            file_path = "tests//resources//test_file.txt"
            file_input = create_input(input_type)
            file_input.add_file_path(file_path)
            file_input.get_houses()
            raise TestError

        # Act/Assert
        self.assertRaises(TestError, helper)

    def test_get_houses_1(self):
        # Arrange
        input_type = InputType.StringInput
        string = "text"

        # Act & Assert
        string_input = create_input(input_type)
        string_input.add_string(string)
        self.assertRaises(BadInputFormatError, string_input.get_houses)

    def test_get_houses_2(self):
        # Arrange
        input_type = InputType.StringInput
        string = "5x5 (6, 1)"

        # Act & Assert
        string_input = create_input(input_type)
        string_input.add_string(string)
        self.assertRaises(BadHouseCoordinatesError, string_input.get_houses)

    def test_get_houses_3(self):
        # Arrange
        input_type = InputType.StringInput
        string = "5x5 (3, 2)"

        # Act
        string_input = create_input(input_type)
        string_input.add_string(string)
        houses = string_input.get_houses()

        # Assert
        self.assertEqual(houses[0].X, 3)
        self.assertEqual(houses[0].Y, 2)

    def test_get_houses_4(self):
        # Arrange
        input_type = InputType.FileReadInput
        file_path = "tests//resources//test_file.txt"

        # Act
        file_input = create_input(input_type)
        file_input.add_file_path(file_path)
        houses = file_input.get_houses()

        # Assert
        self.assertEqual(len(houses), 2)
        self.assertEqual(houses[0].X, 1)
        self.assertEqual(houses[0].Y, 3)
        self.assertEqual(houses[1].X, 4)
        self.assertEqual(houses[1].Y, 4)

class TestError(Exception):
    """Used only for testing purposes"""

if __name__ == '__main__':
    unittest.main()
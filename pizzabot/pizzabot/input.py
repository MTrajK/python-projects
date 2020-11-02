import sys
import re
from enum import Enum
from pizzabot.house import House
from pizzabot.errors import NoInputError, BadInputFormatError, BadHouseCoordinatesError, NotSupportedInputTypeError, MissingPropertyError


class InputType(Enum):
    """All existing input classes"""
    SysArgvInput = 0
    ConsoleReadInput = 1
    FileReadInput = 2
    StringInput = 3


class Input:
    """Base class for all types of inputs"""

    def __parse_input(self, text_input: str) -> list['House']:
        """Converts the input string into a list of houses"""
        # remove all spaces for simpler/smaller regex
        text_input = text_input.replace(" ", "")

        # regex explanation:
        #   - first part ^\d+x\d+: find exactly one NUMBERxNUMBER pattern in the begining
        #   - second part (\(\d+\,\d+\))+$: after that find one or more (NUMBER,NUMBER) patterns till the end
        whole_regex = "^\d+x\d+(\(\d+\,\d+\))+$"
        grid_regex = "^\d+x\d+"
        coordinates_regex = "(\d+\,\d+)"

        match = re.search(whole_regex, text_input)

        if not match:
            raise BadInputFormatError("Wrong format, respect the following format: \"NUMxNUM (NUM, NUM) (NUM, NUM)\"")

        grid_input = re.findall(grid_regex, text_input)[0].split("x")
        grid_size = [int(el) for el in grid_input]

        houses_input = re.findall(coordinates_regex, text_input)
        houses = []

        for house in houses_input:
            house_coords = [int(el) for el in house.split(",")]

            if (house_coords[0] > grid_size[0]) or (house_coords[1] > grid_size[1]):
                raise BadHouseCoordinatesError("One of the houses is outside of the grid, all of them must be inside the grid.")

            houses.append(House(house_coords[0], house_coords[1]))

        return houses

    def get_houses(self) -> list['House']:
        """Gets an input and pares the same input"""
        text_input = self._get_input()
        return self.__parse_input(text_input)


class SysArgvInput(Input):
    """Class that works with CLI parameters input"""

    def _get_input(self) -> str:
        """Gets the CLI parameter value"""
        if len(sys.argv) < 2:
            raise NoInputError("There is no input, enter the grid size and coordinates.")

        return sys.argv[1]


class ConsoleReadInput(Input):
    """Class that waits for user to enter the text"""

    def _get_input(self) -> str:
        """Waits for user to enter the text"""
        return input()


class FileReadInput(Input):
    """Class that works with files"""

    def __init__(self):
        self.file_path = None

    def _get_input(self) -> str:
        """Reads a file, file_path should be added using add_file_path() method"""
        if self.file_path is None:
            raise MissingPropertyError("Add the file path using the add_file_path() method.")

        with open(self.file_path, 'r') as input_file:
            string = input_file.readline()

        return string

    def add_file_path(self, file_path: str) -> None:
        """Adds file_path BEFORE calling _get_input() method"""
        self.file_path = file_path


class StringInput(Input):
    """Class that works with a string added from the code"""

    def __init__(self):
        self.string = None

    def _get_input(self) -> str:
        """Returns the string value, string should be added using add_string() method"""
        if self.string is None:
            raise MissingPropertyError("Add the string value using the add_string() method.")

        return self.string

    def add_string(self, string: str) -> None:
        """Adds string BEFORE calling _get_input() method"""
        self.string = string


def create_input(input_type: 'InputType') -> 'Input':
    """Factory method for creating an input object"""
    all_input_types = {
        InputType.SysArgvInput: SysArgvInput,
        InputType.ConsoleReadInput: ConsoleReadInput,
        InputType.FileReadInput: FileReadInput,
        InputType.StringInput: StringInput
    }

    if input_type not in all_input_types:
        raise NotSupportedInputTypeError("Only the input types from InputType enum can be used.")

    return all_input_types[input_type]()
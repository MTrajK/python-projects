import math
from pizzabot.house import House

class Bot():
    """Class that holds the main pizzabot logic"""

    def __init__(self, input: 'Input'):
        self.input = input

    def get_instructions(self) -> list['Instruction']:
        """Gets the input, finds the path and retruns the instructions"""
        houses = self.input.get_houses()
        path = self.__find_path(houses)
        return self.__create_instructions(path)

    def get_text_instructions(self) -> str:
        """Converts the result from get_instructions into string"""
        instructions = self.get_instructions()
        return "".join([instruction.short_description for instruction in instructions])

    def __find_path(self, houses: list['House']) -> list['House']:
        """Finds the path using the nearest neighbor algorithm"""
        current = House(0, 0)
        visited = set()
        path = [current]

        for house in range(len(houses)):
            nearest_index = self.__find_nearest(current, houses, visited)
            visited.add(nearest_index)
            current = houses[nearest_index]
            path.append(current)

        return path

    def __find_nearest(self, current: 'House', houses: list['House'], visited: set[int]) -> int:
        """Finds the closest house to the current house (only searching the non-visited houses)"""
        nearest_index = -1
        nearest_distance = math.inf

        for house_index in range(len(houses)):
            distance = current.distance(houses[house_index])
            if (house_index not in visited) and (distance < nearest_distance):
                nearest_index = house_index
                nearest_distance = distance

        return nearest_index

    def __create_instructions(self, path: list['House']) -> list['Instruction']:
        """Iterates the path and takes the instructions between neighboring houses"""
        instructions = []

        for house_index in range(len(path) - 1):
            instructions.extend(path[house_index].instructions(path[house_index + 1]))

        return instructions
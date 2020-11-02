
class InputError(Exception):
    """Base exception class for input errors"""

class NoInputError(InputError):
    """Missing input exception"""

class BadInputFormatError(InputError):
    """Not following the input format exception"""

class BadHouseCoordinatesError(InputError):
    """Coordinates out of the grid size"""

class NotSupportedInputTypeError(Exception):
    """The input type doesn't exist still"""

class MissingPropertyError(Exception):
    """Need this property to execute methods"""

class NotSupportedInstructionError(Exception):
    """The instruction doesn't exist still"""
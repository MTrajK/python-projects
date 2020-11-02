from boilerplate.logic.helper import H
from boilerplate.logic.main_logic import ML
import unittest

class TestHelperMethods(unittest.TestCase):

    def test_H(self):
        # Arrange
        expected_result = "boilerplate.logic.helper.H"

        # Act
        result = H()

        # Assert
        self.assertEqual(result, expected_result)

class TestMainLogicMethods(unittest.TestCase):

    def test_ML(self):
        # Arrange
        expected_result = "boilerplate.logic.main_logic.ML calls (boilerplate.logic.helper.H) and (boilerplate.utils.common.C)"

        # Act
        result = ML()

        # Assert
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()

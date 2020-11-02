from boilerplate.utils.common import C
import unittest

class TestCommonMethods(unittest.TestCase):

    def test_C(self):
        # Arrange
        expected_result = "boilerplate.utils.common.C"

        # Act
        result = C()

        # Assert
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
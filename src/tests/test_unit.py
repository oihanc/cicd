import unittest
from unittest.mock import patch

from cicd_oihanc import print_hello_world, count_to_n


class TestFunctions(unittest.TestCase):

    def test_print_hello_world(self):
        with patch("builtins.print") as mock_print:
            print_hello_world()
            mock_print.assert_called_once_with("Hello World!")

    def test_count_to_n(self):
        result = count_to_n(5)
        self.assertEqual(result, [0, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
"""UnitTest."""
import unittest
from main import root

class PlayerTest(unittest.TestCase):
    """Tests for `player.py`."""

    def test_is_output_hw(self):
        """Is the output of your Python Application what you expect?"""
        self.assertTrue(root() == "Hello World perro!")

if __name__ == '__main__':
    unittest.main()

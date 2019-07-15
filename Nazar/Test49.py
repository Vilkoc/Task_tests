import unittest
import Task49


class SeventhTest(unittest.TestCase):
    def test_seven(self):
        self.assertEqual(Task49.num("hello2 3 4"), ['2', '3', '4'])


if __name__ == "__main__":
    unittest.main()

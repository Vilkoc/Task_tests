import unittest
import Task7


class SecondTest(unittest.TestCase):
    def test_two(self):
        self.assertEqual(Task7.lst(3, 5), [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]])


if __name__ == '__main__':
    unittest.main()
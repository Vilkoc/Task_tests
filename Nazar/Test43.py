import unittest
import Task43


class SixthTest(unittest.TestCase):
    def test_six(self):
        self.assertEqual(list(map(Task43.square, [x for x in range(1, 11)])), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])


if __name__ == "__main__":
    unittest.main()

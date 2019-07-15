import unittest
import Task55


class TenthTest(unittest.TestCase):
    def test_ten(self):
        self.assertEqual(Task55.numbers(100), '0, 35, 70')


if __name__ == '__main__':
    unittest.main()

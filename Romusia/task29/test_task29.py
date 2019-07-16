import unittest
import task29


class Task5Test(unittest.TestCase):
    def test_upper(self):

        self.assertEqual("odd", task29.task29())


if __name__ == '__main__':
    unittest.main()

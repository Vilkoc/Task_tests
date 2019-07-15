import unittest
import Task25


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Task25.convert(2), '2')


if __name__ == '__main__':
    unittest.main()

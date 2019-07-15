import unittest
import Task37


class FifthTest(unittest.TestCase):
    def test_five(self):
        self.assertEqual(Task37.func(), [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])


if __name__ == '__main__':
    unittest.main()

import unittest
import task35


class Task35Test(unittest.TestCase):
    def test_upper(self):

        self.assertEqual(task35.printvalues(), [1, 4, 9, 16, 25, 36, 49, 64, 81, \
                                                100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])


if __name__ == '__main__':
    unittest.main()

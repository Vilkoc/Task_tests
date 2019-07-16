import unittest
import task11


class Task5Test(unittest.TestCase):
    def test_upper(self):

        tmp = task11.task11()
        self.assertEqual(tmp, ['1111'])


if __name__ == '__main__':
    unittest.main()

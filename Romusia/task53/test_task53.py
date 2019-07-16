import unittest
import task53


class Task41Test(unittest.TestCase):
    def test_upper(self):

        self.assertEqual(task53.recur_fibo(9), 34)


if __name__ == '__main__':
    unittest.main()

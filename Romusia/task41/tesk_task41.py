import unittest
import task41


class Task41Test(unittest.TestCase):
    def test_upper(self):

        self.assertEqual(task41.task41(), "Yes")


if __name__ == '__main__':
    unittest.main()

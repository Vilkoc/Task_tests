import unittest
import task17


class Task5Test(unittest.TestCase):
    def test_upper(self):
        self.assertEqual(task17.task17(), 250)


if __name__ == '__main__':
    unittest.main()

import unittest
import task5


class Task5Test(unittest.TestCase):
    def test_upper(self):
        tmp = task5.qwerty('qwertyu')
        self.assertEqual(tmp.print_String(), "QWERTYU")


if __name__ == '__main__':
    unittest.main()

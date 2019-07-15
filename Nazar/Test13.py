import unittest
import Task13


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Task13.lm('hello234'), ('Numbers: 3', 'Letters: 5'))


if __name__ == "__main__":
    unittest.main()

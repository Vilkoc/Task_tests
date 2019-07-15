import unittest
import Task19


class ThirdTest(unittest.TestCase):
    def test_three(self):
        self.assertEqual(Task19.sort(
            [('Json', '19', '85'), ('John', '20', '90'), ('Jony', '17', '95'), ('Jony', '17', '93'),
             ('Json', '21', '85')]),
                         [('John', '20', '90'), ('Jony', '17', '93'), ('Jony', '17', '95'), ('Json', '19', '85'), ('Json', '21', '85')])


if __name__ == '__main__':
    unittest.main()

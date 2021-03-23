import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class SquareRootTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator())

    def test_squareroot(self):
        test_data = CsvReader('Unit Test Square Root.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.sqrt(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()

import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class PowerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator())

    def test_power(self):
        test_data = CsvReader('Unit Test Power.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.pwr(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()

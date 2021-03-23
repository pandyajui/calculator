import math
from CsvReader import CsvReader
def addition(a, b):
    c = float(a) + float(b)
    return c


def subtraction(a, b):
    c = float(b) - float(a)
    return c


def multiplication(a, b):
    c = float(a) * float(b)
    return c


def division(a, b):
    c = float(b) / float(a)
    return c


def square(a):
    c = a ** 2
    return c


def squareroot(a):
    c = float(math.sqrt(a))
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sq(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(a)
        return self.result


class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass




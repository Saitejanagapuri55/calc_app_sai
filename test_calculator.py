import pytest
from calculator import Calculator
from faker import Faker

fake = Faker()

def test_add():
    calc = Calculator()
    a = fake.random_int()
    b = fake.random_int()
    assert calc.add(a, b) == a + b

def test_subtract():
    calc = Calculator()
    a = fake.random_int()
    b = fake.random_int()
    assert calc.subtract(a, b) == a - b

def test_multiply():
    calc = Calculator()
    a = fake.random_int()
    b = fake.random_int()
    assert calc.multiply(a, b) == a * b

def test_divide():
    calc = Calculator()
    a = fake.random_int(min=1)  # Ensuring non-zero
    b = fake.random_int(min=1)  # Ensuring non-zero
    assert calc.divide(a, b) == a / b

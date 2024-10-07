import pytest
from calculator import calculator
from faker import Faker

fake = Faker()

@pytest.mark.parametrize("operation", ['add', 'subtract', 'multiply', 'divide', 'unknown'])
def test_calculator_operations(operation):
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)

    if operation == 'add':
        expected = f"The result of {a} add {b} is equal to {a + b}"
    elif operation == 'subtract':
        expected = f"The result of {a} subtract {b} is equal to {a - b}"
    elif operation == 'multiply':
        expected = f"The result of {a} multiply {b} is equal to {a * b}"
    elif operation == 'divide':
        if b == 0:
            expected = "An error occurred: Cannot divide by zero"
        else:
            expected = f"The result of {a} divide {b} is equal to {a / b}"
    else:
        expected = f"Unknown operation: {operation}"

    assert calculator(str(a), str(b), operation) == expected

@pytest.mark.parametrize("a, b, operation, expected", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),
])
def test_calculator(a, b, operation, expected):
    """Tests the calculator function for various operations."""
    assert calculator(a, b, operation) == expected

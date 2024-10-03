from main import calculate

def test_calculate(a, b, operation):
    result = calculate(a, b, operation)
    # Add checks depending on the operation type and expected results
    if operation == 'add':
        assert result == f"The result of {a} add {b} is equal to {a + b}"
    elif operation == 'subtract':
        assert result == f"The result of {a} subtract {b} is equal to {a - b}"
    elif operation == 'multiply':
        assert result == f"The result of {a} multiply {b} is equal to {a * b}"
    elif operation == 'divide':
        if b != 0:
            assert result == f"The result of {a} divide {b} is equal to {a / b}"
        else:
            assert result == "An error occurred: Cannot divide by zero"

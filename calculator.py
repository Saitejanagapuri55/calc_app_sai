def calculator(a, b, operation):
    """
    Performs basic arithmetic operations.

    Parameters:
    a (str): The first number as a string.
    b (str): The second number as a string.
    operation (str): The operation to perform (add, subtract, multiply, divide).

    Returns:
    str: A string describing the result of the operation or an error message.
    """
    try:
        # Convert inputs to float for calculation
        a = float(a)
        b = float(b)
    except ValueError:
        return f"Invalid number input: {a} or {b} is not a valid number."

    # Perform the requested operation and return formatted string
    if operation == 'add':
        return f"The result of {int(a)} add {int(b)} is equal to {int(a + b)}"
    elif operation == 'subtract':
        return f"The result of {int(a)} subtract {int(b)} is equal to {int(a - b)}"
    elif operation == 'multiply':
        return f"The result of {int(a)} multiply {int(b)} is equal to {int(a * b)}"
    elif operation == 'divide':
        if b == 0:
            return "An error occurred: Cannot divide by zero"
        return f"The result of {int(a)} divide {int(b)} is equal to {int(a / b)}"
    else:
        return f"Unknown operation: {operation}"

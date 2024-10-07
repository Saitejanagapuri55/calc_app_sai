def calculate_and_print(a_string, b_string, operation_string):
    try:
        a = float(a_string)  # Convert input strings to float
        b = float(b_string)
    except ValueError:
        print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
        return

    if operation_string == 'add':
        result = a + b
        print(f"The result of {a_string} add {b_string} is equal to {int(result)}")  # Convert to int for display
    elif operation_string == 'subtract':
        result = a - b
        print(f"The result of {a_string} subtract {b_string} is equal to {int(result)}")  # Convert to int for display
    elif operation_string == 'multiply':
        result = a * b
        print(f"The result of {a_string} multiply {b_string} is equal to {int(result)}")  # Convert to int for display
    elif operation_string == 'divide':
        if b == 0:
            print("An error occurred: Cannot divide by zero")
        else:
            result = a / b
            print(f"The result of {a_string} divide {b_string} is equal to {int(result)}")  # Convert to int for display
    else:
        print(f"Unknown operation: {operation_string}")

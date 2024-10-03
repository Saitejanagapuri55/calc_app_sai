import argparse

def calculate(a, b, operation):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return f"Invalid number input: {a} or {b} is not a valid number."

    if operation == 'add':
        return f"The result of {a} add {b} is equal to {a + b}"
    elif operation == 'subtract':
        return f"The result of {a} subtract {b} is equal to {a - b}"
    elif operation == 'multiply':
        return f"The result of {a} multiply {b} is equal to {a * b}"
    elif operation == 'divide':
        if b == 0:
            return "An error occurred: Cannot divide by zero"
        return f"The result of {a} divide {b} is equal to {a / b}"
    else:
        return f"Unknown operation: {operation}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument("a")
    parser.add_argument("b")
    parser.add_argument("operation")
    args = parser.parse_args()

    result = calculate(args.a, args.b, args.operation)
    print(result)

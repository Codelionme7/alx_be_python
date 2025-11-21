@"
def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.
    Returns a float result, or None for invalid operations or division by zero.
    """
    if operation == "add":
        return float(num1 + num2)
    elif operation == "subtract":
        return float(num1 - num2)
    elif operation == "multiply":
        return float(num1 * num2)
    elif operation == "divide":
        if num2 == 0:
            return None
        return float(num1 / num2)
    else:
        return None
"@ > arithmetic_operations.py

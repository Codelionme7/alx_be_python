def safe_divide(numerator, denominator):
    """
    Performs division with error handling for zero division
    and non-numeric inputs.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
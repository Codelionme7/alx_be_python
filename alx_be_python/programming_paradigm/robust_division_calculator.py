# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division with error handling for zero division
    and non-numeric inputs.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # This block runs if the user tries to divide by 0
        return "Error: Cannot divide by zero."

    except ValueError:
        # This block runs if the user inputs text (like "ten") instead of numbers
        return "Error: Please enter numeric values only."
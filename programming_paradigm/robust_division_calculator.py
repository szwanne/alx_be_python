def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    else:
        f"The result of the division is {result:.1f}"

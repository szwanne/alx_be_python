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
        return round(result, 1)

class Calculator:
    # Class attribute shared across all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.
        It doesn't access or modify the class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that accesses the class attribute before multiplying.
        It can access class-level data using cls.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

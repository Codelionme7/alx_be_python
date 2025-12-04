# class_static_methods_demo.py

class Calculator:
    # Class attribute accessible by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Does not need access to the class or instance.
        It behaves like a regular function belonging to the Calculator namespace.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Receives the class (cls) as the first argument.
        It can access class attributes like 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
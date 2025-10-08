class pure_calc:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b 
    
    def divide(self, a, b):
        if b == 0:
            # Tests expect a ValueError with this exact message
            raise ValueError("Division by zero is not allowed")
        return a / b
    
from abc import ABC, abstractmethod
import re
#parsing
#tokenixing or lexer
#evaluatinf by engine
class Operator(ABC):

    @abstractmethod
    def calculate(self, left, right):
        pass

class ArithmeticOperator(Operator):

    def __init__(self, operation):
        self.operation = operation

    def handle_unsupported_operation(self):
        """Handles unsupported operations by raising a ValueError."""
        raise ValueError(f"Unsupported operation: {self.operation}")

    def calculate(self, left, right):
        if self.operation == "+":
            return left + right
        elif self.operation == "-":
            return left - right
        elif self.operation == "*":
            return left * right
        elif self.operation == "/":
            return left / right
        else:
            self.handle_unsupported_operation()

class RegexOperator(Operator):
    """
    Handles regex matching operations.
    """
    def calculate(self, left, pattern):
        return bool(re.match(pattern, str(left)))

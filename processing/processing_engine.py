from processing.parser_lexer import Lexer, Parser
from processing.operators_handlers import ArithmeticOperator, RegexOperator

class ProcessingEngine:
    def __init__(self, equation):
        self.equation = equation

    def calculate(self, node, message):

        if isinstance(node.value, int):  # Numeric literal
            return node.value

        if node.value == "ATTR":
            return message["value"]

        if node.value in ("+", "-", "*", "/"):  # Arithmetic operations
            left = self.calculate(node.left, message)
            right = self.calculate(node.right, message)
            operator = ArithmeticOperator(node.value)
            return operator.calculate(left, right)


        elif node.value == "Regex":  # Regex operations
            left = self.calculate(node.left, message)
            pattern = node.right.value
            operator = RegexOperator()
            return operator.calculate(left, pattern)


        else:
            raise ValueError(f"Unsupported operation: {node.value}")

    def process_message(self, message):
        """
        Parse the equation, build the AST, and evaluate it.
        """
        lexer = Lexer(self.equation)
        parser = Parser(lexer)
        ast = parser.parse()  # Build the AST
        return self.calculate(ast, message)  # calculate the AST




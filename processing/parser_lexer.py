from tokenization import (Token, INTEGER, PLUS, MINUS,
                          MUL, DIV, LPAREN, RPAREN, EOF, REGEX, IDENTIFIER, COMMA, STRING)

class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Operator,Operand,+ or num
        self.left = left    # Left node
        self.right = right  # Right node

    def __repr__(self):
        return f"ASTNode({self.value}, {self.left}, {self.right})"

class Lexer:
    def __init__(self, text):
        # input, e.g. "1*5 + 3 * 1"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable."""
        # Move to the next character in the text.
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None # Indicates end of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        # Parse an integer from the current position in the text.
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def identifier(self):
        # Parse an identifier (sequence of letters, numbers, or underscores).
        result = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        return result

    def string(self):
        # Parse a string (text between double quotes).
        result = ''
        self.advance()  # Skip the opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        self.advance()  # Skip the closing quote
        return result

    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            # Check for digit and return an INTEGER token.
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            # Check for letters and return an identifier or a special keyword.
            if self.current_char.isalpha():
                identifier = self.identifier()
                if identifier == "Regex":
                    return Token(REGEX, "Regex")
                elif identifier == "ATTR":
                    return Token(IDENTIFIER, "ATTR")
                else:
                    raise Exception(f"Unknown identifier: {identifier}")

            # Check for operators and return the corresponding token.
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            # Check for parentheses and return the corresponding tokens.
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')

            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')

            if self.current_char == ',':
                self.advance()
                return Token(COMMA, ',')

            # Check for strings enclosed in single quotes or double quotes
            if self.current_char in ('"', "'"):
                quote_type = self.current_char  # Capture the type of quote
                self.advance()  # Skip the opening quote
                result = ''
                while self.current_char is not None and self.current_char != quote_type:
                    result += self.current_char
                    self.advance()
                if self.current_char == quote_type:
                    self.advance()  # Skip the closing quote
                    return Token(STRING, result)
                else:
                    raise Exception("Unterminated string literal")

            raise Exception('Invalid character')

        return Token(EOF, None) # Return an EOF token when the end of the text is reached

#asts for tokens from lexer
class Parser:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Expected token {token_type}, got {self.current_token.type}")

    """factor : INTEGER | "(" expression ")" | ID"""
    def factor(self):

        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return ASTNode(token.value)
        elif token.type == IDENTIFIER:  # Handle ATTR
            self.eat(IDENTIFIER)
            return ASTNode("ATTR")
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()
        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
            elif token.type == DIV:
                self.eat(DIV)
            node = ASTNode(token.value, left=node, right=self.factor())
        return node

    def expr(self):
        """expr : term ((PLUS | MINUS) term)* | REGEX"""
        if self.current_token.type == REGEX:
            self.eat(REGEX)
            self.eat(LPAREN)
            left = self.factor()
            self.eat(COMMA)
            right = self.current_token.value  # Pattern as a string
            self.eat(STRING)
            self.eat(RPAREN)
            return ASTNode("Regex", left=left, right=ASTNode(right))

        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)
            node = ASTNode(token.value, left=node, right=self.term())
        return node

    def parse(self):
        """Build the AST."""
        return self.expr()


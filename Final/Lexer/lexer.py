# Martin Helmut Domínguez Alvarez
# A01701813
# Examen Final

import re


class Lexer(object):
    """docstring for Lexer."""
    # store tokens
    tokens = []

    def __init__(self, arg):
        super(Lexer, self).__init__()
        self.arg = arg

    def tokenize(self):

        # word list
        code = self.arg
        tokens = self.tokens
        inputs = []

        # DELETE DEFAULT PY COMMENTS
        for index, piece in enumerate(code):
            pieces = piece.split()
            if len(pieces) > 1:
                for element in pieces:
                    inputs.append(element.lower())
            else:
                inputs.append(piece.lower())

        for piece in inputs:
            element = piece.lower()

            exceptions = ['\t', '\n', '', ' ']
            boolean = ['#t', '#f']

            if element == '':
                pass
            # Types
            elif element == "int":
                tokens.append(["INT", element])
            elif element == "bool":
                tokens.append(["BOOL", element])

            # Assignment
            elif element == '=':
                tokens.append(["=", element])
            elif element == 'print':
                tokens.append(["PRINT", element])

            # If
            elif element == 'if':
                tokens.append(["IF", element])
            elif element == 'then':
                tokens.append(["THEN", element])
            elif element == 'end':
                tokens.append(["END", element])

            elif element in '&<+*':
                tokens.append(["OPERATOR", element])  # ALL OPERATORS

            # Boolean
            elif element in boolean:
                tokens.append(["BOOLEAN", element])

            # Symbols
            elif element == '(':
                tokens.append(["(", element])
            elif element == ')':
                tokens.append([")", element])

            # Numbers
            elif element in "-":
                tokens.append(["-", element])
            elif re.match('^[0-9]+$', element):
                tokens.append(["INTEGER", element])

            # Identifiers
            elif re.match('^[ \w+]', element):
                tokens.append(["IDENTIFIER", element])

            # Exceptions
            elif element in exceptions:
                continue
            elif re.match('^[ \t]+', element):
                continue

            else:
                # pass
                raise ValueError('Token no valido', element)

        return tokens

        # for x in tokens:
        #     print(x)

        def get_tokens(self):
            return self.tokens

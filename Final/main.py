import Lexer.lexer as lexer
# from LL_Parser import LLParserTable
from LL_Parser import LLParser
import tokenize
import sys

# Martin Helmut Domínguez Alvarez
# A01701813


def main():

    # Read test.lang

    pieces = []
    with tokenize.open(sys.argv[1]) as file:
        tokens = tokenize.generate_tokens(file.readline)
        for token in tokens:
            pieces.append(token.string)

    # Lexer

    # print(pieces)

    lex = lexer.Lexer(pieces)
    tokens = lex.tokenize()

    LL1_parser = LLParser.LLParser(tokens)
    LL1_parser.analize()


main()

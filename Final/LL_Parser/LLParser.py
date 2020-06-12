# Martín Helmut Domínguez Alvarez
# A01701813
# Examen Final

from collections import defaultdict
from LL_Parser import LLParserTable
import csv
import sys


def peek_stack(stack):
    if stack:
        return stack[-1]


def showParse(token, stack, symbols, action, operand):
    print("Token=", token, "Stack= ", stack, "Symbols= ", symbols, "Action", action, operand, "\n")


class LLParser(object):
    """docstring forLRParser."""

    def __init__(self, arg):
        super(LLParser, self).__init__()
        self.arg = arg

    items = defaultdict(list)

    table = LLParserTable.LLParseTable
    parser_table = table.fill_table('./Data/parser_table.csv')

    def analize(self):

        parser_table = self.parser_table
        tokens = self.arg

        stack = []
        stackInput = []
        tokens.append(["$", "$"])

        lexerTokens = tokens[::-1]

        # print("STACK TOKENS", lexerTokens)

        found = False
        error = False

        stack.append("$")
        stackInput.append("$")
        stack.append(self.table.non_terminals[0])

        # --------------------

        # print(parser_table)

        input_top = lexerTokens.pop()
        input_element = input_top[0].lower()

        while(peek_stack(stack) != "$"):

            state = peek_stack(stack)
            print("STACK", stack, "INPUT", input_element)

            if(state == input_element):
                input_top = peek_stack(lexerTokens)
                input_element = input_top[0].lower()
                # print("ACCEPTED SYMBOL. NEW SYMBOL: ", input_element)
                lexerTokens.pop()
                stack.pop()

            elif state not in self.table.non_terminals:
                raise ValueError(f'Error. Existe un terminal inesperado={state}')

            # Si es un NO TERMINAL
            elif(self.table.break_item(self.parser_table, state, input_element)):
                production = self.table.break_item(self.parser_table, state, input_element)
                # print("Se encontró algo:", production)
                stack.pop()
                self.table.items_to_stack(production, stack)
                # print("STACK", stack)

        # print(input_element)
        if(peek_stack(stack) == input_element):
            print("STACK", stack, "INPUT", input_element)
            print("Terminado. Se ha reconocido el código de entrada")

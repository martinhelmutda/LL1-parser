# Martín Helmut Domínguez Alvarez
# A01701813
# Examen Final

from collections import defaultdict
import csv
import sys


class LLParseTable():
    """docstring forGotos."""

    # def __init__(self, arg):
    #     superGotos, self).__init__()
    #     self.arg=arg

    items = defaultdict(list)
    non_terminals = ['program', 'opt-declaration-list', 'opt-statement-list', 'declaration', 'type',
                     'statement', 'assignment', 'do-print', 'condition', 'expression', 'expression-aux', 'simple-expression']

    def fill_table(file):
        data = csv.reader(open(file, 'r'), delimiter=",")
        items = defaultdict(list)
        symbols = defaultdict(list)

        for row in data:
            symbols[row[1]] = ({'TERMINAL': row[1], 'PRODUCTION': row[2]})
            items[row[0]].append(symbols[row[1]])

        # print(items['18'])
        return items

    def break_item(items, non_terminal, input):
        item = items[str(non_terminal)]
        res = None

        for sub in item:
            if sub['TERMINAL'] == input:
                res = sub
                table_state = res['PRODUCTION']
                return table_state

        if(not res):
            raise ValueError(f'Error, no existe transición del estado: {non_terminal} bajo símbolo: {input}')

    def items_to_stack(production, stack):
        elements = production.split()
        elements = elements[2:]

        while(elements):
            last_element = peek_stack(elements)
            if(last_element != "''"):
                stack.append(last_element)

            elements.pop()

        return stack

    # def items_to_stack(arg):
    #     pass


def peek_stack(stack):
    if stack:
        return stack[-1]

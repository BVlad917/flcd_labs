import re

from production import Production


class Grammar:
    def __init__(self, input_file):
        self.__read_file(input_file)

    @property
    def terminals(self):
        return self.__terminals

    @property
    def non_terminals(self):
        return self.__non_terminals

    @property
    def productions(self):
        return self.__productions

    def productions_for_non_terminal(self, non_terminal):
        return next(p for p in self.__productions if p.left_hand_side == non_terminal)

    def __read_file(self, input_file):
        def parse_grammar_elem(string):
            return string.lstrip('{').rstrip('}').split(',')

        with open(input_file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line[0] == '#':
                continue  # comment line
            elif line[0] == 'G':
                elems = line.replace(' ', '').split('=')[1].lstrip('(').rstrip(')')
                elems = [split_str.lstrip('{').rstrip('}') for split_str in re.split(r'},', elems)]
                self.__non_terminals = parse_grammar_elem(elems[0])
                self.__terminals = parse_grammar_elem(elems[1])
                self.__productions = [Production(p) for p in parse_grammar_elem(elems[2])]
                self.__starting_state = parse_grammar_elem(elems[3])[0]

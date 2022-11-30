from configuration import Configuration


class DescendantRecursiveParser:
    def __init__(self, grammar, w):
        self.__grammar = grammar
        self.__w = w
        self.__configuration = Configuration(grammar.starting_symbol)
        self.__production_index = [0]

    def solve(self):
        pass

    def expand(self):
        top = self.__configuration.pop_input_stack()
        production = top.super_productions[self.__production_index[-1]]
        self.__configuration.push_on_working_stack(production)
        self.__configuration.push_list_on_input_stack(production.rhs[::-1])

    def advance(self):
        top = self.__configuration.pop_input_stack()
        self.__configuration.push_on_working_stack(top)
        self.__configuration.increment_seq_pos()

    def momentary_insuccess(self):
        pass

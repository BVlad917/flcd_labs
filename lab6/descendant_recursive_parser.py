from configuration import Configuration
from state_type import StateType


class DescendantRecursiveParser:
    def __init__(self, grammar, w):
        self.__grammar = grammar
        self.__w = w
        self.__configuration = Configuration(grammar.starting_symbol)

    def solve(self):
        pass

    def expand(self):
        top_input_stack = self.__configuration.pop_input_stack()
        non_terminal = top_input_stack[0]
        if len(top_input_stack) > 1:
            self.__configuration.push_on_input_stack(top_input_stack[1:])
        super_production = self.__grammar.find_super_production(non_terminal.name)
        first_simple_production = super_production.rhs_head
        self.__configuration.push_on_working_stack(first_simple_production)
        self.__configuration.push_on_input_stack(first_simple_production.rhs)

    def advance(self):
        top_input_stack = self.__configuration.pop_input_stack()
        terminal = top_input_stack[0]
        if len(top_input_stack) > 1:
            self.__configuration.push_on_input_stack(top_input_stack[1:])
        self.__configuration.push_on_working_stack(terminal)
        self.__configuration.increment_seq_pos()

    def momentary_insuccess(self):
        self.__configuration.current_state = StateType.BACK_STATE

    def another_try(self):
        pass

    def another_try1(self):
        pass

    def another_try2(self):
        pass

    def another_try3(self):
        pass

    @property
    def configuration(self):
        return self.__configuration

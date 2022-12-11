from state_type import StateType


class Configuration:
    """
    Representation for the configuration used in the Recursive Descendant Parsing Algorithm.
    Contains the following:
        - current_state: one of NORMAL, BACK, FINAL, ERROR
        - current_seq_pos: the current position in the input string (i.e., w)
        - working_stack: list containing simple productions or terminals
        - input_stack: list of lists, each contains non-terminals (corresponding to super productions) or terminals
    """

    def __init__(self, starting_symbol):
        """
        Args:
            starting_symbol: NonTerminal representing the starting symbol's super production
        """
        self.__current_state = StateType.NORMAL_STATE
        self.__current_seq_pos = 1
        self.__working_stack = []
        self.__input_stack = [[starting_symbol]]

    def push_on_working_stack(self, elem):
        self.__working_stack.append(elem)

    def pop_working_stack(self):
        return self.__working_stack.pop()

    def peek_working_stack(self):
        return self.__working_stack[-1]

    def peek_input_stack(self):
        return self.__input_stack[-1]

    def push_on_input_stack(self, elem):
        self.__input_stack.append(elem)

    def pop_input_stack(self):
        return self.__input_stack.pop()

    def increment_seq_pos(self):
        self.__current_seq_pos += 1

    def decrement_seq_pos(self):
        self.__current_seq_pos -= 1

    def is_input_stack_empty(self):
        return len(self.__input_stack) == 0

    def is_working_stack_empty(self):
        return len(self.__working_stack) == 0

    @property
    def current_state(self):
        return self.__current_state

    @current_state.setter
    def current_state(self, new_state):
        self.__current_state = new_state

    @property
    def current_seq_pos(self):
        return self.__current_seq_pos

    @property
    def working_stack(self):
        return self.__working_stack

    @property
    def input_stack(self):
        return self.__input_stack

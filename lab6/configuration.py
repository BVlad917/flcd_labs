from state_type import StateType


class Configuration:
    def __init__(self, starting_symbol):
        self.__current_state = StateType.NORMAL_STATE
        self.__current_seq_pos = 1
        self.__working_stack = []
        self.__input_stack = [starting_symbol]

    def push_on_working_stack(self, elem):
        self.__working_stack.append(elem)

    def push_list_on_input_stack(self, elem):
        self.__input_stack.extend(elem)

    def pop_input_stack(self):
        return self.__input_stack.pop()

    def increment_seq_pos(self):
        self.__current_seq_pos += 1

from configuration import Configuration
from parser_output import ParserOutput
from state_type import StateType
from symbols.symbol_type import SymbolType


class DescendantRecursiveParser:
    """
    Descendant Recursive Parser Algorithm. Implements the main function of the algorithm:
        - EXPAND: when head of input stack is a non-terminal and we have NORMAL current state
        - ADVANCE: when head of input stack is a terminal, this terminal matches the current symbol
        from the input, and the current state is NORMAL
        - MOMENTARY INSUCCESS: when head of input stack is a terminal, this terminal DOES NOT
        match the current symbol from the input, and the current state is NORMAL
        - BACK: when head of working stack is a terminal and the current state is BACK
        - ANOTHER TRY: when head of working stack is a non-terminal and the current state is BACK
        - SUCCESS: when the input stack is empty, the input sequence has been traversed, and
        the current state is NORMAL
    """
    def __init__(self, grammar, w):
        self.__grammar = grammar
        self.__w = w
        self.__configuration = Configuration(grammar.starting_symbol)

    def solve(self):
        """
        Implement the Descendant Recursive Algorithm by calling the algorithm's specific
        functions (expand, advance, momentary insuccess, back, another try, success) in
        the appropriate cases
        """
        while self.__configuration.current_state not in [StateType.FINAL_STATE, StateType.ERROR_STATE]:
            if self.__configuration.current_state == StateType.NORMAL_STATE:
                current_index_in_w = self.__configuration.current_seq_pos
                input_stack_is_empty = self.__configuration.is_input_stack_empty()
                if current_index_in_w == len(self.__w) + 1 and input_stack_is_empty:
                    self.success()
                else:
                    top_list_input_stack = self.__configuration.peek_input_stack()
                    top_input_stack = top_list_input_stack[0]
                    current_seq_pos = self.__configuration.current_seq_pos
                    if top_input_stack.symbol_type == SymbolType.NON_TERMINAL:
                        self.expand()
                    elif current_seq_pos - 1 < len(self.__w) and top_input_stack.name == self.__w[current_seq_pos - 1]:
                        self.advance()
                    else:
                        self.momentary_insuccess()
            else:
                top_working_stack = self.__configuration.peek_working_stack()
                if top_working_stack.symbol_type == SymbolType.TERMINAL:
                    self.back()
                else:
                    self.another_try()
        if self.__configuration.current_state == StateType.ERROR_STATE:
            return "ERROR - SEQUENCE NOT ACCEPTED", None
        else:
            return "SEQUENCE ACCEPTED", ParserOutput(self.__configuration)

    def expand(self):
        """
        Expand method of the Descendant Recursive Parser.
        Pops the head of the input stack (which is a non-terminal corresponding to a super production),
        finds the super production corresponding to this head, takes its first simple production,
        and pushes it on the working stack and its right-hand side on the input stack
        """
        top_input_stack = self.__configuration.pop_input_stack()
        non_terminal = top_input_stack[0]
        if len(top_input_stack) > 1:
            # elements of the input stack are lists => might need to push the rest of the head element
            # back on the input stack
            self.__configuration.push_on_input_stack(top_input_stack[1:])
        super_production = self.__grammar.find_super_production(non_terminal.name)
        first_simple_production = super_production.rhs_head
        self.__configuration.push_on_working_stack(first_simple_production)
        self.__configuration.push_on_input_stack(first_simple_production.rhs)

    def advance(self):
        """
        Advance method of the Descendant Recursive Parser.
        Pops the head of the input stack (which is a terminal), pushes this terminal on the working
        stack, and increments the configuration's sequence position
        """
        top_input_stack = self.__configuration.pop_input_stack()
        terminal = top_input_stack[0]
        if len(top_input_stack) > 1:
            # elements of the input stack are lists => might need to push the rest of the head element
            # back on the input stack
            self.__configuration.push_on_input_stack(top_input_stack[1:])
        self.__configuration.push_on_working_stack(terminal)
        self.__configuration.increment_seq_pos()

    def momentary_insuccess(self):
        """
        Momentary insuccess method of the Descendant Recursive Parser.
        Sets the current state of the configuration to BACK
        """
        self.__configuration.current_state = StateType.BACK_STATE

    def back(self):
        """
        Back method of the Descendant Recursive Parser.
        Pops the head of the working stack (which at this point can only be a Terminal)
        and pushes it back in the input stack (in a list)
        """
        self.__configuration.decrement_seq_pos()
        top_working_stack = self.__configuration.pop_working_stack()
        self.__configuration.push_on_input_stack([top_working_stack])
        self.__reconstruct_simple_production_rhs()  # todo: remove from here and put it in main loop

    def another_try(self):
        """
        Another try method of the Descendant Recursive Parser.
        The top of the working stack can only be a SimpleProduction at this point.
        Runs one of 3 another try sub-methods (depending on the case):
            - another_try1: if the simple production which is the head of the working stack
            has a not None "next_production" attribute
            - another_try3: if the configuration's current sequence position is 1 and the
            parent of the simple production from the head of the working stack is the starting super production
            - another_try2: in all other cases
        """
        conf = self.__configuration
        top_working_stack = conf.peek_working_stack()
        if top_working_stack.next_simple_production is not None:
            self.another_try1()
        elif conf.current_seq_pos == 1 and top_working_stack.parent == self.__grammar.starting_symbol:
            self.another_try3()
        else:
            self.another_try2()

    def another_try1(self):
        """
        Another try 1 method of the Descendant Recursive Parser
        Pops the input stack, pushes on the working stack the next simple production of the working stack's
        head, pushes on the input stack the rhs of this next simple production, and changes the
        configuration's current state to NORMAL
        """
        self.__configuration.current_state = StateType.NORMAL_STATE
        self.__configuration.pop_input_stack()
        top_working_stack = self.__configuration.pop_working_stack()
        next_simple_production = top_working_stack.next_simple_production
        self.__configuration.push_on_working_stack(next_simple_production)
        self.__configuration.push_on_input_stack(next_simple_production.rhs)

    def another_try2(self):
        """
        Another try 2 method of the Descendant Recursive Parser
        Pops the input stack, pops the working stack, and pushes on the input stack
        the parent (i.e., a super production) of the working stack's head
        """
        self.__configuration.pop_input_stack()
        top_working_stack = self.__configuration.pop_working_stack()
        top_working_stack_parent = top_working_stack.parent
        self.__configuration.push_on_input_stack([top_working_stack_parent])

    def another_try3(self):
        """
        Another try 3 method of the Descendant Recursive Parser
        Pops the input stack, pops the working stack, and sets the configuration's state to ERROR
        """
        self.__configuration.pop_input_stack()
        self.__configuration.pop_working_stack()
        self.__configuration.current_state = StateType.ERROR_STATE

    def success(self):
        """
        Success method of the Descendant Recursive Parser
        Sets the configuration's state to FINAL
        """
        self.__configuration.current_state = StateType.FINAL_STATE

    def __reconstruct_simple_production_rhs(self):
        """
        Method which checks if the first n elements from the input stack correspond
        to the RHS of the working stack's head. If this is true, the n elements (which
        currently are lists of length 1) are combined into one single flattened list
        and pushed back on the input stack.
        This method is useful to make sure the another try 1 method is working correctly. It should be used
        after using the BACK method
        """
        conf = self.__configuration
        top_ws = conf.peek_working_stack()
        if top_ws.symbol_type == SymbolType.TERMINAL or len(conf.input_stack) < len(top_ws.rhs):
            return
        possible_rhs = [conf.pop_input_stack() for _ in top_ws.rhs]
        cond1 = all(len(elem) == 1 for elem in possible_rhs)
        cond2 = True
        for e1, e2 in zip(top_ws.rhs, possible_rhs):
            if e1.symbol_type == SymbolType.NON_TERMINAL:
                e1 = self.__grammar.find_super_production(e1.name)
            if e1 != e2[0]:
                cond2 = False
        if not cond1 or not cond2:
            for elem in reversed(possible_rhs):
                conf.push_on_input_stack(elem)
            return
        flat_possible_rhs = [item for sublist in possible_rhs for item in sublist]
        self.__configuration.push_on_input_stack(flat_possible_rhs)

    @property
    def configuration(self):
        return self.__configuration

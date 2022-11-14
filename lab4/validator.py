class FaValidator:
    def __init__(self, fa):
        self.__fa = fa

    def validate(self):
        """
        Run all validators
        """
        self.__validate_states_in_transitions()
        self.__validate_results_in_transitions()
        self.__validate_accepted_in_transitions()
        self.__validate_initial_state()
        self.__validate_final_states()

    def __validate_initial_state(self):
        """
        Validate that the initial state is used as starting state at least once
        """
        all_starts = {t.get_state() for t in self.__fa.transitions}
        initial_state = {self.__fa.initial_state}
        states_int = all_starts.intersection(initial_state)
        assert len(states_int) == len(initial_state), "ERROR: Initial state must appear as start at least once"

    def __validate_final_states(self):
        """
        Validate that the final states are used as resulting state at least once
        """
        all_results = set([t.get_result() for t in self.__fa.transitions])
        all_final_states = set(self.__fa.final_states)
        states_int = all_results.intersection(all_final_states)
        assert len(states_int) == len(all_final_states), "ERROR: Final states must appear as results at least once"

    def __validate_states_in_transitions(self) -> None:
        """
        Validate that the states which appear in the transitions are valid states (i.e., were specified in the file)
        """
        transition_states = set([t.get_state() for t in self.__fa.transitions])
        fa_states = set(self.__fa.states)
        states_int = transition_states.intersection(fa_states)
        assert len(states_int) == len(transition_states), "ERROR: Invalid state(s) given in transitions starting states"

    def __validate_results_in_transitions(self) -> None:
        """
        Validate that all results in the transitions are valid states (i.e., were specified in the file)
        """
        transition_results = set([t.get_result() for t in self.__fa.transitions])
        fa_results = set(self.__fa.states)
        states_int = transition_results.intersection(fa_results)
        assert len(states_int) == len(transition_results), "ERROR: Invalid state(s) given in transitions results"

    def __validate_accepted_in_transitions(self) -> None:
        """
        Validate that all symbols which are used as <accepted> are valid symbols (i.e., appear in the alphabet)
        """
        transition_accepted = set([t.get_accepted() for t in self.__fa.transitions])
        fa_alphabet = set(self.__fa.alphabet)
        accepted_int = transition_accepted.intersection(fa_alphabet)
        assert len(accepted_int) == len(fa_alphabet), "ERROR: Invalid symbol(s) given in transitions accepted"

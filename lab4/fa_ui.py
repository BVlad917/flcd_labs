from finite_automata import FiniteAutomata


class FaMenu:
    """
    UI interface (menu) for the Finite Automata program
    """
    def __init__(self, fa: FiniteAutomata):
        self.__fa = fa

    def run_menu(self) -> None:
        cmds = {'1': self.__print_states, '2': self.__print_alphabet, '3': self.__print_transitions,
                '4': self.__print_initial_state, '5': self.__print_final_states, '6': self.__print_if_is_dfa,
                '7': self.__print_is_sequence_accepted}
        while True:
            self.__print_menu()
            cmd = input("Enter your command: ").strip()
            if cmd == 'x':
                print("Exiting...")
                break
            elif cmd not in cmds.keys():
                print("Invalid command.")
            else:
                cmds[cmd]()

    @staticmethod
    def __print_menu() -> None:
        print(f"1. Print all states\n"
              f"2. Print alphabet\n"
              f"3. Print transitions\n"
              f"4. Print initial state\n"
              f"5. Print final state\n"
              f"6. Check if FA is DFA\n"
              f"7. Check if sequence is accepted by the FA\n"
              f"x. Exit\n")

    def __print_is_sequence_accepted(self) -> None:
        seq = input("Please enter a sequence: ")
        if self.__fa.is_sequence_accepted(seq):
            print(f"Yes, the sequence '{seq}' is accepted by the language.")
        else:
            print(f"No, the sequence '{seq}' is NOT accepted by the language.")

    def __print_if_is_dfa(self) -> None:
        """
        Display on the screen a message which tells the user if the input FA is a DFA or not
        """
        if self.__fa.is_dfa():
            print("Yes, the given FA is a DFA")
        else:
            print("No, the given FA is NOT a DFA")

    def __print_states(self) -> None:
        """
        Print the states of the FA
        """
        print("STATES: ", end='')
        print(self.__fa.states)

    def __print_alphabet(self) -> None:
        """
        Print the alphabet of the FA
        """
        print("ALPHABET: ", end='')
        print(self.__fa.alphabet)

    def __print_transitions(self) -> None:
        """
        Print the transitions of the FA
        """
        print("TRANSITIONS:")
        for t in self.__fa.transitions:
            print(t)

    def __print_initial_state(self) -> None:
        """
        Print the initial state of the FA
        """
        print("INITIAL STATE: ", end='')
        print(self.__fa.initial_state)

    def __print_final_states(self) -> None:
        """
        Print the final states of the FA
        """
        print("FINAL STATE: ", end='')
        print(self.__fa.final_states)



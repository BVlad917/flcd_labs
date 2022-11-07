class FiniteAutomata:
    def __init__(self, input_file_path):
        self.__states = None
        self.__alphabet = None
        self.__transitions = None
        self.__is = None
        self.__fs = None
        self.__read_from_file(input_file_path)

    def is_sequence_accepted(self, seq):
        pass

    def __read_from_file(self, file_path):
        with open(file_path, 'r') as f:
            for line in f.read().splitlines():
                if not len(line) or line.strip()[0] == '#':
                    continue
                elems_type, elems = line.split('=')[0], line.split('=')[1]
                if elems_type == "Q": self.__states = elems
                elif elems_type == "S": self.__alphabet = elems
                elif elems_type == "T": self.__transitions = elems
                elif elems_type == "IS": self.__is = elems[0]
                elif elems_type == "FS": self.__fs = elems
                else: raise ValueError("ERROR: Invalid elements type.")

    def run_menu(self):
        cmds = {'1': self.__print_states, '2': self.__print_alphabet, '3': self.__print_transitions,
                '4': self.__print_initial_state, '5': self.__print_final_states}
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
    def __print_menu():
        print(f"1. Print all states\n"
              f"2. Print alphabet\n"
              f"3. Print transitions\n"
              f"4. Print initial state\n"
              f"5. Print final state\n"
              f"x. Exit\n")

    def __print_states(self):
        print("STATES: ", end='')
        print(self.__states)

    def __print_alphabet(self):
        print("ALPHABET: ", end='')
        print(self.__alphabet)

    def __print_transitions(self):
        print("TRANSITIONS: ", end='')
        print(self.__transitions)

    def __print_initial_state(self):
        print("INITIAL STATE: ", end='')
        print(self.__is)

    def __print_final_states(self):
        print("FINAL STATE: ", end='')
        print(self.__fs)

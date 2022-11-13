from collections import defaultdict
from typing import List

from transition import Transition


class FiniteAutomata:
    """
    Finite automata representation. The finite automata is read from an input file, and it stores the following:
    the states, the alphabet, the transitions, the initial state, and the final state
    """

    def __init__(self, input_file_path: str) -> None:
        self.__states = None
        self.__alphabet = None
        self.__transitions = None
        self.__is = None
        self.__fs = None
        self.__read_from_file(input_file_path)

    def is_dfa(self) -> bool:
        """
        Check if the FA is a DFA or not
        :return: True if the FA is a DFA; False otherwise
        """
        groups = defaultdict(list)
        for t in self.__transitions:
            groups[(t.get_state(), t.get_accepted())].append(t.get_result())
        if any([len(group) > 1 for group in groups.values()]):
            return False
        return True

    def is_sequence_accepted(self, seq: str) -> bool:
        """
        Check if a given sequence is accepted by the language or not
        :param seq: sequence to be checked; string
        :return: True if the sequence is accepted by the language; False otherwise
        """
        stack = [(seq, self.__is)]
        while stack:
            current_seq, current_state = stack.pop()
            if not len(current_seq) and current_state in self.__fs:
                return True
            elif not len(current_seq):
                continue
            acc_neighbors = self.__get_accepted_neighbors_of_state(current_state, current_seq[0])
            for n in acc_neighbors:
                stack.append((current_seq[1:], n.get_result()))
        return False

    def __get_accepted_neighbors_of_state(self, state: str, accepted: str) -> List[Transition]:
        """
        Return all transitions which can be reached from the state <state> with <accepted>
        """
        all_neighbors = [t for t in self.__transitions if t.get_state() == state]
        return [n for n in all_neighbors if n.get_accepted() == accepted]

    def __read_from_file(self, file_path: str) -> None:
        """
        Read a finite automata from an input file.
        :param file_path: the path of the file where the FA is stored; string
        """
        with open(file_path, 'r') as f:
            for line in f.read().splitlines():
                if not len(line) or line.strip()[0] == '#':
                    continue
                elems_type, elems = line.split('=')[0], line.split('=')[1].split(' ')
                if elems_type == "Q":
                    self.__states = elems
                elif elems_type == "S":
                    self.__alphabet = elems
                elif elems_type == "T":
                    self.__transitions = self.__parse_transitions(elems)
                elif elems_type == "IS":
                    self.__is = elems[0]
                elif elems_type == "FS":
                    self.__fs = elems
                else:
                    raise ValueError("ERROR: Invalid elements type.")

    @staticmethod
    def __parse_transitions(transitions_list: List[str]) -> List[Transition]:
        """
        Parse a list of transitions from the file input and return a list of Transition instances
        :param transitions_list: list of transitions represented as strings; e.g., "(q0, 1, q1)"
        :return: list of Transition instances
        """
        parsed_transitions = []
        for t in transitions_list:
            t = t.lstrip('(').rstrip(')').split(',')
            parsed_transitions.append(Transition(t[0], t[1], t[2]))
        return parsed_transitions

    def get_states(self):
        return self.__states

    def get_alphabet(self):
        return self.__alphabet

    def get_transitions(self):
        return self.__transitions

    def get_initial_state(self):
        return self.__is

    def get_final_states(self):
        return self.__fs

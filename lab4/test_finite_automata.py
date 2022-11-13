from unittest import TestCase

from finite_automata import FiniteAutomata


class TestFiniteAutomata(TestCase):
    def test_is_sequence_accepted(self):
        # integers FA
        int_fa = FiniteAutomata("./fa.in")
        # check valid sequences
        self.assertTrue(int_fa.is_sequence_accepted("123"))
        self.assertTrue(int_fa.is_sequence_accepted("+123"))
        self.assertTrue(int_fa.is_sequence_accepted("-123"))
        self.assertTrue(int_fa.is_sequence_accepted("0"))
        self.assertTrue(int_fa.is_sequence_accepted("+1"))
        # check invalid sequences
        self.assertFalse(int_fa.is_sequence_accepted(""))
        self.assertFalse(int_fa.is_sequence_accepted("-"))
        self.assertFalse(int_fa.is_sequence_accepted("0123"))
        self.assertFalse(int_fa.is_sequence_accepted("12a3"))

        # sequences with at least 2 consecutive zeros
        cons_0_fa = FiniteAutomata("./fa2.in")
        # check valid sequences
        self.assertTrue(cons_0_fa.is_sequence_accepted("00"))
        self.assertTrue(cons_0_fa.is_sequence_accepted("001"))
        self.assertTrue(cons_0_fa.is_sequence_accepted("111111100"))
        # check invalid sequences
        self.assertFalse(cons_0_fa.is_sequence_accepted("00a"))
        self.assertFalse(cons_0_fa.is_sequence_accepted("0"))
        self.assertFalse(cons_0_fa.is_sequence_accepted("0101010110101010"))
        self.assertFalse(cons_0_fa.is_sequence_accepted(""))

    def test_is_dfa(self):
        int_fa = FiniteAutomata("./fa.in")  # integers FA, DFA
        self.assertTrue(int_fa.is_dfa())
        cons_0_fa = FiniteAutomata("./fa2.in")  # sequences with at least 2 consecutive zeros, NFA
        self.assertFalse(cons_0_fa.is_dfa())
        last_fa = FiniteAutomata("./fa3.in")  # seq. with one 1 and ['0', '1'] as the only characters, DFA
        self.assertTrue(last_fa.is_dfa())

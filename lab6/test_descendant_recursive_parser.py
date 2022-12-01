import unittest

from descendant_recursive_parser import DescendantRecursiveParser
from grammar import Grammar
from state_type import StateType
from symbols.non_terminal import NonTerminal
from symbols.terminal import Terminal


class TestDescendantRecursiveParser(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Grammar("./inputs/grammar3.in")
        self.w = "aacbc"
        self.parser = DescendantRecursiveParser(self.g, self.w)

    def test_expand(self):
        self.parser.expand()
        conf = self.parser.configuration
        self.assertEquals(conf.current_state, StateType.NORMAL_STATE)
        self.assertEquals(conf.current_seq_pos, 1)
        self.assertEquals(len(conf.working_stack), 1)
        self.assertEquals(conf.working_stack[-1].name, "S1")
        self.assertEquals(len(conf.input_stack), 1)
        self.assertEquals(len(conf.input_stack[-1]), 4)
        self.assertEquals(conf.input_stack[-1][0], Terminal("a"))
        self.assertEquals(conf.input_stack[-1][1], NonTerminal("S"))
        self.assertEquals(conf.input_stack[-1][2], Terminal("b"))
        self.assertEquals(conf.input_stack[-1][3], NonTerminal("S"))

    def test_advance(self):
        self.parser.expand()
        self.parser.advance()
        conf = self.parser.configuration
        self.assertEquals(conf.current_state, StateType.NORMAL_STATE)
        self.assertEquals(conf.current_seq_pos, 2)
        self.assertEquals(len(conf.working_stack), 2)
        self.assertEquals(conf.working_stack[0].name, "S1")
        self.assertEquals(conf.working_stack[1].name, "a")
        self.assertEquals(len(conf.input_stack), 1)
        self.assertEquals(len(conf.input_stack[-1]), 3)
        self.assertEquals(conf.input_stack[-1][0], NonTerminal("S"))
        self.assertEquals(conf.input_stack[-1][1], Terminal("b"))
        self.assertEquals(conf.input_stack[-1][2], NonTerminal("S"))

    def test_momentary_insuccess(self):
        self.parser.expand()
        self.parser.advance()
        self.parser.expand()
        self.parser.advance()
        self.parser.expand()
        self.parser.momentary_insuccess()
        conf = self.parser.configuration
        self.assertEquals(conf.current_state, StateType.BACK_STATE)

    def test_all_functions(self):
        self.parser.expand()
        self.parser.advance()
        self.parser.expand()
        self.parser.advance()
        self.parser.expand()
        self.parser.momentary_insuccess()

        conf = self.parser.configuration
        print()
        print(conf.current_state)
        print(conf.current_seq_pos)
        print(conf.working_stack)
        print(conf.input_stack)

import unittest

from grammar import Grammar
from symbols.non_terminal import NonTerminal
from symbols.terminal import Terminal


class GrammarTests(unittest.TestCase):
    def test_read_grammar_non_terminals(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(len(g.non_terminals), 3)
        self.assertIn(NonTerminal("S"), g.non_terminals)
        self.assertIn(NonTerminal("A"), g.non_terminals)
        self.assertIn(NonTerminal("B"), g.non_terminals)

    def test_read_grammar_terminals(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(len(g.terminals), 2)
        self.assertIn(Terminal("a"), g.terminals)
        self.assertIn(Terminal("b"), g.terminals)

    def test_read_grammar_super_productions(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(len(g.super_productions), 3)
        # first super production
        p1 = g.super_productions[0]
        self.assertEquals(p1.name, "S")
        self.assertEquals(p1.lhs, [NonTerminal("S")])
        self.assertEquals(p1.rhs_length, 1)
        # second super production
        p2 = g.super_productions[1]
        self.assertEquals(p2.name, "A")
        self.assertEquals(p2.lhs, [NonTerminal("A")])
        self.assertEquals(p2.rhs_length, 3)
        # third super production
        p3 = g.super_productions[2]
        self.assertEquals(p3.name, "B")
        self.assertEquals(p3.lhs, [NonTerminal("B")])
        self.assertEquals(p3.rhs_length, 2)

    def test_read_grammar_starting_symbol(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(g.starting_symbol, NonTerminal("S"))

    def test_is_cfg(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertTrue(g.is_cfg())

    def test_non_terminal_productions(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(len(g.simple_productions_for_non_terminal("S")), 1)
        self.assertEquals(len(g.simple_productions_for_non_terminal("A")), 3)
        self.assertEquals(len(g.simple_productions_for_non_terminal("B")), 2)
        self.assertRaises(ValueError, g.simple_productions_for_non_terminal, "C")

    def test_simple_productions(self):
        g = Grammar("./inputs/grammar1.in")
        p = g.super_productions[1]
        self.assertEquals(p.name, "A")
        p1 = p.rhs_head
        self.assertEquals(p1.name, "A1")
        self.assertEquals(p1.rhs, [Terminal("a"), NonTerminal("A")])
        self.assertEquals(p1.parent, p)
        p2 = p1.next_simple_production
        self.assertEquals(p2.name, "A2")
        self.assertEquals(p2.rhs, [Terminal("b"), NonTerminal("B")])
        self.assertEquals(p2.parent, p)
        p3 = p2.next_simple_production
        self.assertEquals(p3.name, "A3")
        self.assertEquals(p3.rhs, [Terminal("b")])
        self.assertEquals(p3.parent, p)
        p4 = p3.next_simple_production
        self.assertIsNone(p4)
        self.assertEquals(p1.parent, p2.parent)
        self.assertEquals(p1.parent, p3.parent)
        self.assertEquals(p2.parent, p3.parent)

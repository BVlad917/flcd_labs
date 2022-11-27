import unittest

from grammar import Grammar
from production import Production
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

    def test_read_grammar_productions(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(len(g.productions), 6)
        p1 = Production([NonTerminal("S")], [Terminal("a"), NonTerminal("A")])
        p2 = Production([NonTerminal("A")], [Terminal("a"), NonTerminal("A")])
        p3 = Production([NonTerminal("A")], [Terminal("b"), NonTerminal("B")])
        p4 = Production([NonTerminal("A")], [Terminal("b")])
        p5 = Production([NonTerminal("B")], [Terminal("b"), NonTerminal("B")])
        p6 = Production([NonTerminal("B")], [Terminal("b")])
        self.assertIn(p1, g.productions)
        self.assertIn(p2, g.productions)
        self.assertIn(p3, g.productions)
        self.assertIn(p4, g.productions)
        self.assertIn(p5, g.productions)
        self.assertIn(p6, g.productions)

    def test_read_grammar_starting_symbol(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(g.starting_symbol, NonTerminal("S"))

    def test_is_cfg(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertTrue(g.is_cfg())

    def test_non_terminal_productions(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(len(g.productions_for_non_terminal("S")), 1)
        self.assertEquals(len(g.productions_for_non_terminal("A")), 3)
        self.assertEquals(len(g.productions_for_non_terminal("B")), 2)
        self.assertRaises(ValueError, g.productions_for_non_terminal, "C")

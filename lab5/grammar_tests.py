import unittest

from grammar import Grammar


class GrammarTests(unittest.TestCase):
    def test_read_grammar_file(self):
        g = Grammar("./inputs/grammar1.in")
        self.assertEquals(g.non_terminals, ['S', 'A', 'B'])
        self.assertEquals(g.terminals, ['a', 'b'])
        

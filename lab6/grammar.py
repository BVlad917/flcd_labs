from productions.super_production import SuperProduction
from symbols.epsilon import Epsilon
from symbols.non_terminal import NonTerminal
from symbols.symbol_type import SymbolType
from symbols.terminal import Terminal


class Grammar:
    """
    Grammar representation which holds the following:
    - terminals: list of Terminals instances
    - non_terminals: list of NonTerminals instances
    - super_productions: list of SimpleProduction instances
    - starting_symbol: NonTerminal instance
    """
    def __init__(self, input_file):
        self.__read_file(input_file)

    def is_cfg(self):
        """
        Return True if the grammar is a CFG; False otherwise
        """
        super_productions = self.__super_productions
        return all(len(p.lhs) == 1 and p.lhs[0].symbol_type == SymbolType.NON_TERMINAL for p in super_productions)

    def simple_productions_for_non_terminal(self, nt_str: str):
        """
        Return the super_productions corresponding to the given non-terminal string
        """
        corresp_nt = NonTerminal(nt_str)
        if corresp_nt not in self.__non_terminals:
            raise ValueError(f"The given string ({nt_str}) does not correspond to an existing non terminal.")
        all_corresponding_sp = [p for p in self.__super_productions if corresp_nt in p.lhs]
        simple_productions = [sp.all_simple_productions for sp in all_corresponding_sp]
        return [item for sublist in simple_productions for item in sublist]

    @property
    def terminals(self):
        return self.__terminals

    @property
    def non_terminals(self):
        return self.__non_terminals

    @property
    def super_productions(self):
        return self.__super_productions

    @property
    def starting_symbol(self):
        return self.__starting_symbol

    def __parse_symbol_combination_string(self, symbol_comb_str):
        """
        Parse a combination of symbols delimited by "`" and return the list of symbols
        :param symbol_comb_str: string with symbols delimited by "`"; str
        :return: list of Symbol instances
        e.g., input: symbol_comb_str = "a`A"
              output: [NonTerminal("a"), Terminal("A")]
        """
        symbols = []
        for s in symbol_comb_str.split('`'):
            if s == 'ε':
                symbols.append(Epsilon)
                continue
            term, non_term = Terminal(s), NonTerminal(s)
            if term in self.__terminals:
                symbols.append(term)
            elif non_term in self.__non_terminals:
                symbols.append(non_term)
            else:
                raise ValueError(f"Invalid symbol ('{s}') given in '{symbol_comb_str}'")
        return symbols

    def __parse_production_line(self, production_string):
        """
        Parse the given string which represents a production with multiple RHS values delimited by OR ("|")
        :param production_string: string representing a production; str
        :return: list of SimpleProduction instances
        e.g., input: production_string="B~b`B|b"
              output: [SimpleProduction(lhs=[NonTerminal("B")], rhs=[Terminal("b"), NonTerminal(B)]),
                        SimpleProduction(lhs=[NonTerminal("B")], rhs=[NonTerminal("b")])]
        """
        splits = production_string.split('~')
        if len(splits) != 2:
            raise ValueError(f"Incorrect production format for: {production_string}")
        lhs_string, rhs_strings = splits[0], splits[1]
        lhs = self.__parse_symbol_combination_string(lhs_string)
        all_rhs = [self.__parse_symbol_combination_string(rhs_string) for rhs_string in rhs_strings.split('|')]
        super_production = SuperProduction(lhs, all_rhs)
        return super_production

    def __read_file(self, input_file: str):
        """
        Parse the given input file into the current Grammar instance
        :param input_file: input file path; str
        """
        with open(input_file, 'r') as f:
            lines = f.readlines()
        non_comm_lines = [line.strip() for line in lines if len(line.strip()) and line[0] != '#']
        if len(non_comm_lines) < 3:
            raise ValueError("Invalid input file format")
        self.__non_terminals = [NonTerminal(elem) for elem in non_comm_lines[0].split(',')]
        self.__terminals = [Terminal(elem) for elem in non_comm_lines[1].split(',')]
        self.__super_productions = []
        for line in non_comm_lines[2:-1]:
            self.__super_productions.append(self.__parse_production_line(line))
        starting_symbol_nt = NonTerminal(non_comm_lines[-1].strip())
        if starting_symbol_nt not in self.__non_terminals:
            raise ValueError(f'The given starting symbol ("{non_comm_lines[-1].strip()}") is not a non-terminal.')
        self.__starting_symbol = starting_symbol_nt

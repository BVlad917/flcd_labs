from symbols.symbol import Symbol
from symbols.symbol_type import SymbolType


class SimpleProduction(Symbol):
    """
    Class representing a simple production, i.e., a single part of a super production.
    We can look at a lecture's example to understand what a simple production would be:
        Say we have the following (super) production (corresponding to a NonTerminal):
            A -> Gamma_1 | Gamma_2 | ... | Gamma_n
        This (super) production is then broken into n SIMPLE productions:
            A1 -> Gamma_1
            A2 -> Gamma_2
            ...
            An -> Gamma_n

    Thus, a simple productions will hold the following (these are the only necessary things it needs)
        - name: string, e.g., "A1"
        - rhs: list of terminals and non-terminals, corresponding to Gamma_1, e.g., [a, S, b, S]
        - parent: corresponding SuperProduction, e.g., A -> Gamma_1 | Gamma_2 | ... Gamma_n
        - next_production: simple production are linked in a linked list, therefore each simple production
        will hold a reference to the next simple production in the super production, e.g., for simple production
        A1, next_production: A2
    """
    def __init__(self, name, rhs, parent, next_production):
        super().__init__(name)
        self.__rhs = rhs
        self.__parent = parent
        self.__next_simple_production = next_production
        self._ProductionBase__production_type = SymbolType.SIMPLE_PRODUCTION

    @property
    def next_simple_production(self):
        return self.__next_simple_production

    @property
    def rhs(self):
        return self.__rhs

    @property
    def parent(self):
        return self.__parent

    def __str__(self):
        return f'SIMPLE_PRODUCTION("{self.name}")'

    def __eq__(self, other):
        if len(self.rhs) != len(other.rhs) or self.name != other.name:
            return False
        return all(e1 == e2 for e1, e2 in zip(self.rhs, other.rhs))

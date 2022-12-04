from productions.simple_production import SimpleProduction
from symbols.symbol import Symbol
from symbols.symbol_type import SymbolType


class SuperProduction(Symbol):
    """
    Class representing a super production, i.e., the lhs and all the rhs corresponding to a
    non-terminal from the input file.
    We can look at a lecture's example to understand what a super production would be:
        Say we have the following production (corresponding to a NonTerminal):
            A -> Gamma_1 | Gamma_2 | ... | Gamma_n
        This entire thing (lhs + all rhs) will be a SuperProduction. It will then be broken
        into n SimpleProduction's:
            A1 -> Gamma_1
            A2 -> Gamma_2
            ...
            An -> Gamma_n

    Thus, a super production will hold the following:
        - name: e.g., "A"
        - lhs: all symbols from the left-hand side, e.g., [NonTerminal("A")]
        - head: the first simple production in the super production, e.g., NonTerm("A1")
        - length: the number of simple productions the super production holds
    """
    def __init__(self, lhs, all_rhs):
        super().__init__('_'.join(elem.name for elem in lhs))
        self._ProductionBase__production_type = SymbolType.SUPER_PRODUCTION
        self.__lhs = lhs
        self.__link_simple_productions(all_rhs)

    @property
    def lhs(self):
        return self.__lhs

    @property
    def rhs_head(self):
        return self.__head

    @property
    def rhs_length(self):
        return self.__length

    @property
    def all_simple_productions(self):
        """
        Traverse the linked list of simple productions inside the super production and
        return all simple productions
        Return:
            all simple productions from the current super production; list of SimpleProduction instances
        """
        productions = []
        head = self.__head
        while head is not None:
            productions.append(head)
            head = head.next_simple_production
        return productions

    def __link_simple_productions(self, all_rhs):
        """
        Helper function used in the constructor. Links all the given right-hand side elements
        into a linked list of simple productions. Also, sets the super production's "length" and "head" attributes
        """
        self.__length = len(all_rhs)
        prev_production = None
        for idx, rhs in enumerate(reversed(all_rhs)):
            p = SimpleProduction(f"{self.name}{self.__length - idx}", rhs, self, prev_production)
            if idx == len(all_rhs) - 1:
                self.__head = p
            prev_production = p

    def __str__(self):
        string = f"{self.name} --> "
        for p in self.all_simple_productions:
            string += '&'.join(str(e) for e in p.rhs) + ' | '
        return string[:-3]

    def __eq__(self, other):
        if self.name != other.name or len(self.lhs) != len(other.lhs):
            return False
        if not all(e1 == e2 for e1, e2 in zip(self.lhs, other.lhs)):
            return False
        return all(e1 == e2 for e1, e2 in zip(self.all_simple_productions, other.all_simple_productions))
